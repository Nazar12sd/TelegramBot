"""
Конфигурационный файл для Telegram бота
"""

import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Токен бота Telegram (обязательный)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN не найден в переменных окружения. "
        "Пожалуйста, создайте .env файл и добавьте туда токен вашего бота."
    )

# Дополнительные настройки
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Настройки бота
BOT_NAME = os.getenv("BOT_NAME", "Мой Telegram Бот")
BOT_DESCRIPTION = "Базовый Telegram бот на Python"
