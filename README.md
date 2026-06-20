# API Tests Portfolio

Автотесты REST API на Python, Pytest и Requests.  
Проект для портфолио QA Automation.

## Стек

- **Python 3.10+**
- **Pytest** — фреймворк для тестирования
- **Requests** — HTTP-клиент
- **python-dotenv** — переменные окружения

## Быстрый старт

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
pip install -r requirements.txt
pytest tests/ -v -m "not auth"  # тесты, которые не требуют API-ключ в .env
```

## Структура проекта

```
├── conftest.py          # общие фикстуры (base_url, api_posts, api_key)
├── pytest.ini           # настройки pytest (маркеры, verbose по умолчанию)
├── requirements.txt     # зависимости
├── .env.example         # шаблон для переменных окружения
│
├── tests/
│   ├── test_user.py             # тесты с фикстурами (локальные данные)
│   ├── test_discount.py         # parametrize (табличные тесты)
│   ├── test_jsonplaceholder.py  # CRUD-тесты публичного REST API
│   └── test_auth_reqres.py      # тесты авторизации (требует REQRES_API_KEY в .env)
│
└── utils/               # вспомогательные модули (на будущее)
```

## Что тестируется

### JSONPlaceholder API (публичное)
- GET /users, GET /users/{id} — получение списка и структуры
- GET /posts, POST /posts, PUT /posts/{id}, DELETE /posts/{id} — полный CRUD
- GET /comments — вложенные ресурсы, проверка всех элементов через `all()`
- GET /posts/99999 — негативный тест (404)

### Локальные функции
- `calculate_discount(price, percent)` — parametrize, 5 наборов данных
- Работа со списком пользователей через фикстуры и `conftest.py`

### Авторизация (Reqres.in)
- `POST /api/login` — получение JWT-токена
- Негативные тесты: неверный API-ключ (403), отсутствие пароля (400)
- Требует `REQRES_API_KEY` в `.env` (см. `.env.example`)

## Запуск выборочных тестов

```bash
pytest -m api           # только API-тесты
pytest -m "not api"     # только локальные тесты
pytest tests/test_discount.py -v    # конкретный файл
pytest -m auth           # только тесты авторизации, которые требуют API-ключ в .env
pytest -m "not auth"     # тесты, которые не требуют API-ключ в .env
```