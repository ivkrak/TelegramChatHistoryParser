from contextlib import asynccontextmanager

from fastapi import FastAPI
from pyrogram import Client

from settings import settings

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


app = FastAPI(
    title="Parser",
    description="Parser",
    version="0.1",
    lifespan=lifespan
)


@app.get(
    '/',
    description='Получить историю чата'
                ' если одновременно передать chat_id и chat_username,'
                ' то будет смотреть историю чата по chat_id'
                ' !!!Сообщения забираются с конца!!!'
)
async def get_chat_history(
        chat_id: int = None,
        chat_username: str = None,
        offset: int = 0,
        limit: int = 100
):
    messages_history = []
    async for message in tg.get_chat_history(
            chat_id=chat_id if chat_id is not None else chat_username,
            offset=offset,
            limit=limit
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
