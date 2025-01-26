# Chat Parser API

## Description
Chat Parser API is a FastAPI application designed to fetch chat history from Telegram. The application uses the Pyrogram library and supports authentication through an `.env` file.

## Features
- Retrieve chat history by `chat_id` or `chat_username`.
- Return messages with additional information such as text, sender, date, replies, and more.

---

## Installation and Setup

### Requirements
- Python 3.12
- Docker and Docker Compose

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ivkrak/TelegramChatHistoryParser
   cd TelegramChatHistoryParser
   ```

2. **Create a `.env` file**:

   ### Where can I find the `API_ID` and `API_HASH`? You can find them here: https://my.telegram.org/auth.

   Copy the contents of `.env.example` and save them into a `.env` file. Fill in the variables with your data:
   ```env
   API_ID=Your_API_ID
   API_HASH=Your_API_HASH
   PHONE_NUMBER=Your_phone_number
   CLOUD_PASSWORD=Your_cloud_password_if_applicable
   ```

   > **Note**: If you don't need authorization, leave the `API_KEY` empty or don't set it at all.

3. **Build and run using Docker**:
   ```bash
   docker-compose up --build -d
   ```

---

## Endpoints

### `GET /`
#### Description
Fetch chat history.

#### Parameters
- `chat_id` (int, optional) — Chat ID.
- `chat_username` (str, optional) — Chat username.
- `offset` (int, optional) — Offset (default 0).
- `limit` (int, optional) — Number of messages (default 100).

#### Example Request
```bash
curl -X 'GET'\
    'http://localhost:8000/?chat_username=me&offset=0&limit=100'\
    -H 'accept: application/json'\
    -H 'Authorization: Bearer 123'
```

#### Example Response
```json
[
  {
    "id": 1,
    "from_user_id": 12345,
    "from_user_username": "username",
    "text": "Sample message",
    "date": "2023-01-01T12:00:00",
    "reply_to_message_id": null,
    "reply_to_top_message_id": null
  }
]
```

---

## Development

### Local Installation
1. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

2. Run the application:
   ```bash
   python3 main.py
   ```

---

## API Documentation
After starting the application, the documentation will be available at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
