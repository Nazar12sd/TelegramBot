#!/usr/bin/env python3
"""
Простой Telegram бот с использованием requests
"""

import json
import logging
import requests
import time
from config import BOT_TOKEN

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

class SimpleTelegramBot:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}"
        self.offset = 0
    
    def send_message(self, chat_id, text):
        """Отправка сообщения"""
        url = f"{self.api_url}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        try:
            response = requests.post(url, json=payload)
            return response.json()
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения: {e}")
            return None
    
    def get_updates(self):
        """Получение обновлений"""
        url = f"{self.api_url}/getUpdates"
        payload = {'offset': self.offset, 'timeout': 30}
        try:
            response = requests.get(url, params=payload)
            return response.json()
        except Exception as e:
            logger.error(f"Ошибка получения обновлений: {e}")
            return None
    
    def handle_start(self, chat_id, user_name):
        """Обработчик команды /start"""
        message = f"""
👋 Привет, {user_name}!

Добро пожаловать в мой простой Telegram бот!

Я могу:
• Отвечать на ваши сообщения
• Выполнять команды /start и /help
• Помогать с информацией

Используйте /help для просмотра доступных команд.
        """
        self.send_message(chat_id, message.strip())
    
    def handle_help(self, chat_id):
        """Обработчик команды /help"""
        message = """
📋 <b>Доступные команды:</b>

/start - Запустить бота и получить приветствие
/help - Показать это сообщение с помощью

🔹 <b>Как использовать бота:</b>

• Просто отправьте мне любое текстовое сообщение, и я отвечу
• Используйте команды выше для получения дополнительной информации
• Бот работает в режиме 24/7

❓ Если у вас есть вопросы, просто напишите мне!
        """
        self.send_message(chat_id, message.strip())
    
    def handle_time(self, chat_id):
        """Обработчик команды /время"""
        import datetime
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S, %d.%m.%Y")
        message = f"🕐 Текущее время: {current_time}"
        self.send_message(chat_id, message)
    
    def handle_text_message(self, chat_id, user_name, text):
        """Обработчик текстовых сообщений"""
        text_lower = text.lower()
        
        if any(greeting in text_lower for greeting in ['привет', 'hello', 'hi', 'здравствуй']):
            response = f"Привет, {user_name}! 👋 Как дела?"
        elif any(question in text_lower for question in ['как дела', 'что нового', 'как поживаешь']):
            response = "У меня всё отлично! Готов помочь вам. Что вас интересует?"
        elif any(thanks in text_lower for thanks in ['спасибо', 'благодарю', 'thanks']):
            response = "Пожалуйста! Всегда рад помочь! 😊"
        elif any(bye in text_lower for bye in ['пока', 'до свидания', 'bye', 'goodbye']):
            response = "До свидания! Обращайтесь в любое время! 👋"
        elif 'помощь' in text_lower or 'help' in text_lower:
            response = "Конечно помогу! Используйте команду /help для просмотра всех доступных функций."
        else:
            response = (
                f"Получил ваше сообщение: \"{text}\"\n\n"
                f"Спасибо за сообщение! Я простой бот и пока учусь отвечать на разные запросы. "
                f"Используйте /help для просмотра доступных команд."
            )
        
        self.send_message(chat_id, response)
    
    def process_update(self, update):
        """Обработка одного обновления"""
        try:
            if 'message' in update:
                message = update['message']
                chat_id = message['chat']['id']
                user_name = message['from'].get('first_name', 'Пользователь')
                
                if 'text' in message:
                    text = message['text']
                    logger.info(f"Получено сообщение от {user_name} ({chat_id}): {text}")
                    
                    if text == '/start':
                        self.handle_start(chat_id, user_name)
                    elif text == '/help':
                        self.handle_help(chat_id)
                    elif text == '/время':
                        self.handle_time(chat_id)
                    else:
                        self.handle_text_message(chat_id, user_name, text)
        except Exception as e:
            logger.error(f"Ошибка обработки обновления: {e}")
    
    def run(self):
        """Запуск бота"""
        logger.info("Запуск простого Telegram бота...")
        
        while True:
            try:
                updates = self.get_updates()
                if updates and updates.get('ok'):
                    for update in updates.get('result', []):
                        self.process_update(update)
                        self.offset = update['update_id'] + 1
                        
                time.sleep(1)  # Небольшая пауза между запросами
                
            except KeyboardInterrupt:
                logger.info("Бот остановлен пользователем")
                break
            except Exception as e:
                logger.error(f"Общая ошибка: {e}")
                time.sleep(5)  # Пауза при ошибке

if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN не найден!")
        exit(1)
    
    bot = SimpleTelegramBot(BOT_TOKEN)
    logger.info("Бот успешно запущен и готов к работе!")
    bot.run()