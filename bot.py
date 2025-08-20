#!/usr/bin/env python3
"""
Основной файл Telegram бота
"""

import asyncio
import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ExtBot
from telegram import Update
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

async def main():
    """Главная функция для запуска бота"""
    try:
        # Создаем приложение
        logger.info("Запуск Telegram бота...")
        
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Регистрируем обработчики команд
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        
        # Регистрируем обработчик текстовых сообщений
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
        
        # Регистрируем обработчик ошибок
        application.add_error_handler(error_handler)
        
        logger.info("Бот успешно запущен и готов к работе!")
        
        # Запускаем бота
        await application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"Критическая ошибка при запуске бота: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
