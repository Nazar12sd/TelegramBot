#!/usr/bin/env python3
"""
Основной файл Telegram бота
"""

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import BOT_TOKEN
from handlers import start_command, help_command, handle_text_message, error_handler

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Главная функция для запуска бота"""
    try:
        # Создаем Updater
        logger.info("Запуск Telegram бота...")
        
        if not BOT_TOKEN:
            raise ValueError("BOT_TOKEN не найден")
        updater = Updater(token=BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        
        # Регистрируем обработчики команд
        dispatcher.add_handler(CommandHandler("start", start_command))
        dispatcher.add_handler(CommandHandler("help", help_command))
        
        # Регистрируем обработчик текстовых сообщений
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))
        
        # Регистрируем обработчик ошибок
        dispatcher.add_error_handler(error_handler)
        
        logger.info("Бот успешно запущен и готов к работе!")
        
        # Запускаем бота
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        raise

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")