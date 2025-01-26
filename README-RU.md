# Chat Parser API

## Описание
Chat Parser API — это приложение FastAPI, предназначенное для получения истории чатов из Telegram. Оно использует библиотеку Pyrogram и поддерживает аутентификацию через файл `.env`.

## Возможности
- Получение истории чатов по `chat_id` или `chat_username`.
- Возврат сообщений с дополнительной информацией, включая текст, отправителя, дату, ответы и многое другое.

---

## Установка и настройка

### Требования
- Python 3.12.4
- Docker и Docker Compose

### Шаги установки

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ivkrak/TelegramChatHistoryParser
   cd TelegramChatHistoryParser
   ```

2. **Создайте файл `.env`**:

   ### Где найти `API_ID` и `API_HASH`? Их можно получить здесь: https://my.telegram.org/auth.

   Скопируйте содержимое файла `.env.example` и сохраните его как `.env`. Заполните переменные вашими данными:
   ```env
   API_ID=Ваш_API_ID
   API_HASH=Ваш_API_HASH
   PHONE_NUMBER=Ваш_номер_телефона
   CLOUD_PASSWORD=Ваш_облачный_пароль_если_есть
   ```

   > **Примечание**: Если вам не нужна авторизация, не указывайте `API_KEY` или оставьте его пустым.

3. **Соберите и запустите приложение с помощью Docker**:
   ```bash
   docker-compose up --build -d
   ```

---

## Эндпоинты

### `GET /`
#### Описание
Получение истории чата.

#### Параметры
- `chat_id` (int, optional) — ID чата.
- `chat_username` (str, optional) — Имя пользователя чата.
- `offset` (int, optional) — Смещение (по умолчанию 0).
- `limit` (int, optional) — Количество сообщений (по умолчанию 100).

#### Пример запроса
```bash
curl -X 'GET'\
    'http://localhost:8000/?chat_username=me&offset=0&limit=100'\
    -H 'accept: application/json'\
    -H 'Authorization: Bearer 123'
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

### Локальная установка
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
