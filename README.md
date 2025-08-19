# Minesweeper Telegram Bot 🎮

**Сапёр Бот 💣** — это Telegram-бот, который позволяет играть в классическую игру «Сапёр» прямо в чате. Открывай клетки,
отмечай мины и соревнуйся с друзьями! Удобное управление через кнопки, система рейтинга Эло, статистика игроков.

---

## ✨ Возможности

- ⚡ Игровое поле 8x8 с минами
- 🟦 Открытие клеток через интерактивные кнопки
- ⭐ Подсчёт очков и рейтинга игроков
- 👤 Личный профиль с вашей статистикой
- 🏆 Топ-10 игроков по рейтингу

---

## 🛠️ Стек технологий

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-async-blue?logo=telegram)](https://docs.aiogram.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-embedded-lightgrey?logo=sqlite)](https://www.sqlite.org/index.html)
[![python-dotenv](https://img.shields.io/badge/dotenv-env%20config-green)](https://pypi.org/project/python-dotenv/)
[![OS](https://img.shields.io/badge/OS-built--in-lightblue)](https://docs.python.org/3/library/os.html)
[![Logging](https://img.shields.io/badge/Logging-built--in-grey)](https://docs.python.org/3/library/logging.html)

## 📦 Установка

1. Клонируйте репозиторий

```bash
git clone https://github.com/finniy/Minesweeper.git
cd Minesweeper
```

2. Создайте и активируйте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости

```bash
pip install -r requirements.txt
```

4. Укажите токен бота в `.env`

```bash
API_KEY=YOUR_TELEGRAM_BOT_TOKEN
```

5. Запустите бота

```bash
python main.py
```

## 📂 Структура проекта

``` 
Minesweeper/
│
├── app/
│   ├── bot.py
│   ├── bot_instance.py
│   ├── config.py
│   ├── logger.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── players.py
│   │
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── game.py
│   │   ├── home.py
│   │   ├── profile.py
│   │   ├── rating.py
│   │   ├── rules.py
│   │   └── start.py
│   │
│   ├── messages/
│   │   ├── __init__.py
│   │   └── text.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── board.py
│       ├── found_scores.py
│       ├── game_logic.py
│       ├── key.py
│       └── keyboards.py
│
├── images/
│   ├── Photo1.png
│   └── Photo2.png
├── .env
├── .env.template
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 📸 Примеры работы бота

<img src="images/Photo1.png" width="600" style="display: block; margin: auto;">

<img src="images/Photo2.png" width="600" style="display: block; margin: auto;">

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используй, дорабатывай и распространяй с указанием авторства.

---

## 👤 Автор

🚀 **[Перейти к боту в Telegram](https://t.me/SweeperGameBot)**

- GitHub: [@finniy](https://github.com/finniy)
- Telegram: [@fjnnjk](https://t.me/fjnnjk)

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился бот! 😉