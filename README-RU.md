# Chat Parser API

## Описание
Chat Parser API — это FastAPI-приложение для получения истории чатов из Telegram. Приложение использует библиотеку Pyrogram и поддерживает аутентификацию через `.env` файл.

## Функционал
- Получение истории чатов по `chat_id` или `chat_username`.
- Возврат сообщений с дополнительной информацией, включая текст, автора, дату, ответ на сообщение и др.

---

## Установка и настройка

### Требования
- Python 3.12.4
- Docker и Docker Compose

### Шаги для установки

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ivkrak/TelegramChatHistoryParser
   cd TelegramChatHistoryParser
   ```

2. **Создайте файл `.env`**:

   ### Где я могу найти `API_ID` и `API_HASH`? Вы можете найти их здесь: https://my.telegram.org/auth.

   Скопируйте содержимое `.env.example` и сохраните его в файл `.env`. Заполните переменные своими данными:
   ```env
   API_ID=Ваш_API_ID
   API_HASH=Ваш_API_HASH
   PHONE_NUMBER=Ваш_номер_телефона
   CLOUD_PASSWORD=Ваш_облачный_пароль_если_есть
   ```

3. **Сборка и запуск с помощью Docker**:
   ```bash
   docker-compose up --build -d
   ```

---

## Эндпоинты

### `GET /`
#### Описание
Получить историю чата.

#### Параметры
- `chat_id` (int, optional) — ID чата.
- `chat_username` (str, optional) — Username чата.
- `offset` (int, optional) — Смещение (по умолчанию 0).
- `limit` (int, optional) — Количество сообщений (по умолчанию 100).

#### Пример запроса
```bash
curl -X GET "http://localhost:8000/?chat_id=123456&offset=0&limit=10"
```

#### Пример ответа
```json
[
  {
    "id": 1,
    "from_user_id": 12345,
    "from_user_username": "username",
    "text": "Пример сообщения",
    "date": "2023-01-01T12:00:00",
    "reply_to_message_id": null,
    "reply_to_top_message_id": null
  }
]
```

---

## Разработка

### Установка локально
1. Установите зависимости:
   ```bash
   pip install poetry
   poetry install
   ```

2. Запустите приложение:
   ```bash
   python3 main.py
   ```

---

## Документация API
После запуска приложения документация будет доступна по адресу:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

