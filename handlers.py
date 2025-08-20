"""
Обработчики команд и сообщений для Telegram бота
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    try:
        user = update.effective_user
        logger.info(f"Пользователь {user.first_name} ({user.id}) выполнил команду /start")
        
        welcome_message = f"""
👋 Привет, {user.first_name}!

Добро пожаловать в мой Telegram бот!

Я могу:
• Отвечать на ваши сообщения
• Выполнять различные команды
• Помогать с информацией

Используйте /help для просмотра доступных команд.
        """
        
        await update.message.reply_text(
            welcome_message.strip(),
            parse_mode=ParseMode.HTML
        )
        
    except Exception as e:
        logger.error(f"Ошибка в обработчике команды /start: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обработке команды. Попробуйте позже."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    try:
        user = update.effective_user
        logger.info(f"Пользователь {user.first_name} ({user.id}) выполнил команду /help")
        
        help_message = """
📋 <b>Доступные команды:</b>

/start - Запустить бота и получить приветствие
/help - Показать это сообщение с помощью

🔹 <b>Как использовать бота:</b>

• Просто отправьте мне любое текстовое сообщение, и я отвечу
• Используйте команды выше для получения дополнительной информации
• Бот работает в режиме 24/7

❓ Если у вас есть вопросы, просто напишите мне!
        """
        
        await update.message.reply_text(
            help_message.strip(),
            parse_mode=ParseMode.HTML
        )
        
    except Exception as e:
        logger.error(f"Ошибка в обработчике команды /help: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обработке команды. Попробуйте позже."
        )

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    try:
        user = update.effective_user
        message_text = update.message.text
        
        logger.info(f"Получено сообщение от {user.first_name} ({user.id}): {message_text}")
        
        # Простые ответы на ключевые слова
        message_lower = message_text.lower()
        
        if any(greeting in message_lower for greeting in ['привет', 'hello', 'hi', 'здравствуй']):
            response = f"Привет, {user.first_name}! 👋 Как дела?"
            
        elif any(question in message_lower for question in ['как дела', 'что нового', 'как поживаешь']):
            response = "У меня всё отлично! Готов помочь вам. Что вас интересует?"
            
        elif any(thanks in message_lower for thanks in ['спасибо', 'благодарю', 'thanks']):
            response = "Пожалуйста! Всегда рад помочь! 😊"
            
        elif any(bye in message_lower for bye in ['пока', 'до свидания', 'bye', 'goodbye']):
            response = "До свидания! Обращайтесь в любое время! 👋"
            
        elif 'помощь' in message_lower or 'help' in message_lower:
            response = "Конечно помогу! Используйте команду /help для просмотра всех доступных функций."
            
        else:
            # Общий ответ для остальных сообщений
            response = (
                f"Получил ваше сообщение: \"{message_text}\"\n\n"
                f"Спасибо за сообщение! Я базовый бот и пока учусь отвечать на разные запросы. "
                f"Используйте /help для просмотра доступных команд."
            )
        
        await update.message.reply_text(response)
        
    except Exception as e:
        logger.error(f"Ошибка в обработчике текстовых сообщений: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обработке вашего сообщения. Попробуйте позже."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Глобальный обработчик ошибок"""
    logger.error(f"Произошла ошибка: {context.error}")
    
    # Если ошибка связана с обновлением от пользователя
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "Извините, произошла техническая ошибка. Пожалуйста, попробуйте позже."
            )
        except Exception as e:
            logger.error(f"Не удалось отправить сообщение об ошибке: {e}")
