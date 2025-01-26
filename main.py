from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pyrogram import Client

from settings import settings

# Pyrogram Client
tg = Client(
    "parser",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    phone_number=settings.PHONE_NUMBER,
    password=settings.CLOUD_PASSWORD,
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    await tg.start()
    try:
        yield
    finally:
        await tg.stop()


# Bearer Token Security
security = HTTPBearer() if settings.API_KEY else None


async def get_current_token(
        credentials: HTTPAuthorizationCredentials = Security(security) if settings.API_KEY else None
) -> str:
    if settings.API_KEY is None:
        return None  # Skip token validation if API_KEY is None
    token = credentials.credentials
    if token != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing Bearer Token")
    return token


# FastAPI App Initialization
app = FastAPI(
    title="Chat Parser",
    description="Parser for telegram public chats",
    version="0.1",
    lifespan=lifespan,
    openapi_tags=[] if settings.API_KEY is None else None,  # Remove security scheme from OpenAPI if no API_KEY
)


@app.get(
    '/',
    description='Fetch chat history'
                ' if both chat_id and chat_username are provided,'
                ' the chat history will be retrieved using chat_id.'
                ' !!!Messages are fetched from the end!!!'

)
async def get_chat_history(
        chat_id: int = None,
        chat_username: str = None,
        offset: int = 0,
        limit: int = 100,
        _: str = Depends(get_current_token) if settings.API_KEY else None
):
    messages_history = []
    if chat_id is None and chat_username is None:
        raise HTTPException(status_code=400, detail="chat_id or chat_username is required")
    async for message in tg.get_chat_history(
            chat_id=chat_id if chat_id is not None else chat_username,
            offset=offset,
            limit=limit,
    ):
        messages_history.append(
            {
                'id': message.id,
                'from_user_id': message.from_user.id if message.from_user else None,
                'from_user_username': message.from_user.username if message.from_user else None,
                'text': message.text if message.text else None,
                'date': message.date,
                'reply_to_message_id': message.reply_to_message_id if message.reply_to_message_id else None,
                'reply_to_top_message_id': message.reply_to_top_message_id if message.reply_to_top_message_id else None,
            }
        )
    return messages_history


def run():
    import uvicorn
    uvicorn.run('__main__:app', host="0.0.0.0")


if __name__ == "__main__":
    run()
