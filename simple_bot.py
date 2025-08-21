import telebot
from telebot import types
import random
import time

TOKEN = "8352696943:AAERBHk7hBn2iPLkRZlwf_61v8HkJKPKVPI"  # ВСТАВЬ СВОЙ ТОКЕН, ДЕБИЛ
bot = telebot.TeleBot(TOKEN)

# 📦 Хранилище данных
user_stands = {}  # user_id: stand_data
ADMIN_IDS = [2106900629]  # СЮДА ВПИШИ СВОЙ ID, КРЕТИН. УЗНАЙ ЕГО ЧЕРЕЗ @userinfobot

# 🎲 Список стендов
STANDS = {
    "Tusk": {
        "user": "Джонни Джостар",
        "ability": "Создание вращающихся ногтей, способных пробивать пространство",
        "stats": {"power": "B", "speed": "A", "range": "C", "durability": "C", "precision": "B", "potential": "A"},
        "quote": "«Я буду вращаться... пока не достигну бесконечности!»"
    },
    "Ball Breaker": {
        "user": "Джайро Цеппели",
        "ability": "Создание энергии вращения, проникающей через любые барьеры",
        "stats": {"power": "A", "speed": "A", "range": "B", "durability": "B", "precision": "A", "potential": "A"},
        "quote": "«Истинная доблесть джентльмена!»"
    },
    "Oh! Lonesome Me": {
        "user": "Маунтейн Тим",
        "ability": "Превращение в песок и управление им",
        "stats": {"power": "C", "speed": "B", "range": "A", "durability": "D", "precision": "C", "potential": "B"},
        "quote": "«Одиночество - моя сила...»"
    },
    "Scary Monsters": {
        "user": "Доктор Фердинанд/Диего Брандо",
        "ability": "Превращение людей в динозавров",
        "stats": {"power": "A", "speed": "B", "range": "C", "durability": "B", "precision": "C", "potential": "B"},
        "quote": "«Рев древнего мира!»"
    },
    "Cream Starter": {
        "user": "Хот Панц",
        "ability": "Создание и восстановление плоти из крема",
        "stats": {"power": "C", "speed": "B", "range": "D", "durability": "C", "precision": "A", "potential": "B"},
        "quote": "«Красота требует жертв...»"
    },
    "Ticket to Ride": {
        "user": "Люси Стил",
        "ability": "Слияние с предметами и людьми",
        "stats": {"power": "E", "speed": "C", "range": "D", "durability": "E", "precision": "B", "potential": "A"},
        "quote": "«Я должна защитить священный труп...»"
    },
    "Dirty Deeds Done Dirt Cheap": {
        "user": "Фанни Валентайн",
        "ability": "Путешествие между параллельными вселенными",
        "stats": {"power": "C", "speed": "A", "range": "A", "durability": "B", "precision": "B", "potential": "A"},
        "quote": "«Делай грязные дела за гроши!»"
    },
    "D4C Love Train": {
        "user": "Фанни Валентайн",
        "ability": "Перенаправление несчастий на противника",
        "stats": {"power": "A", "speed": "A", "range": "A", "durability": "A", "precision": "A", "potential": "A"},
        "quote": "«Любовь и мир! Любовный поезд!»"
    },
    "In a Silent Way": {
        "user": "Сэндмен",
        "ability": "Создание и контроль звуковых волн",
        "stats": {"power": "B", "speed": "B", "range": "B", "durability": "C", "precision": "A", "potential": "B"},
        "quote": "«Тишина может быть громче крика...»"
    },
    "Hey Ya!": {
        "user": "Поколоко",
        "ability": "Предоставление удачи и моральной поддержки",
        "stats": {"power": "E", "speed": "E", "range": "E", "durability": "E", "precision": "E", "potential": "A"},
        "quote": "«Всё будет хорошо! Всё будет хорошо!»"
    },
    "Tomb of the Boom": {
        "user": "Семья Бум Бум",
        "ability": "Создание и контроль взрывов",
        "stats": {"power": "A", "speed": "B", "range": "B", "durability": "C", "precision": "B", "potential": "B"},
        "quote": "«БУМ! БУМ! БУМ!»"
    },
    "Boku no Rhythm wo Kiitekure": {
        "user": "Оекомова",
        "ability": "Создание ритмичных атак, ускоряющихся со временем",
        "stats": {"power": "B", "speed": "A", "range": "C", "durability": "C", "precision": "B", "potential": "B"},
        "quote": "«Почувствуй мой ритм!»"
    },
    "Wired": {
        "user": "Порк Пай Хэт",
        "ability": "Контроль и усиление страха противника",
        "stats": {"power": "C", "speed": "B", "range": "B", "durability": "D", "precision": "A", "potential": "B"},
        "quote": "«Страх - лучший союзник...»"
    },
    "Mandom": {
        "user": "Ринго Родэгейн",
        "ability": "Возвращение времени на 6 секунд назад",
        "stats": {"power": "C", "speed": "B", "range": "E", "durability": "B", "precision": "A", "potential": "A"},
        "quote": "«Назад во времени...»"
    },
    "Catch the Rainbow": {
        "user": "Блэкмор",
        "ability": "Контроль дождя и создание радужных мостов",
        "stats": {"power": "B", "speed": "A", "range": "A", "durability": "C", "precision": "A", "potential": "B"},
        "quote": "«Поймай радугу...»"
    },
    "Sugar Mountain": {
        "user": "Гигантское Дерево",
        "ability": "Испытание жадности через превращение в золото",
        "stats": {"power": "A", "speed": "E", "range": "E", "durability": "A", "precision": "E", "potential": "A"},
        "quote": "«Жадность ведет к гибели...»"
    },
    "Tatoo You!": {
        "user": "Одиннадцать мужчин",
        "ability": "Создание татуировок, управляющих волей",
        "stats": {"power": "B", "speed": "C", "range": "B", "durability": "D", "precision": "A", "potential": "B"},
        "quote": "«Твоя кожа станет моим холстом!»"
    },
    "Tubular Bells": {
        "user": "Майк О.",
        "ability": "Создание и контроль колокольного звука",
        "stats": {"power": "B", "speed": "B", "range": "B", "durability": "C", "precision": "A", "potential": "B"},
        "quote": "«Звон судьбы!»"
    },
    "20th Century Boy": {
        "user": "Маджента Маджента",
        "ability": "Абсолютная защита в обмен на неподвижность",
        "stats": {"power": "E", "speed": "E", "range": "E", "durability": "A", "precision": "E", "potential": "C"},
        "quote": "«Непобедимая защита!»"
    },
    "Civil War": {
        "user": "Аксель РО",
        "ability": "Вызов чувства вины и грехов противника",
        "stats": {"power": "A", "speed": "B", "range": "A", "durability": "B", "precision": "B", "potential": "A"},
        "quote": "«Твои грехи вернутся к тебе!»"
    },
    "Chocolate Disco": {
        "user": "Д-И-С-К-О",
        "ability": "Создание шоколадных плиток, предсказывающих будущее",
        "stats": {"power": "B", "speed": "B", "range": "B", "durability": "C", "precision": "A", "potential": "A"},
        "quote": "«Будущее в шоколаде!»"
    },
    "THE WORLD": {
        "user": "Диего Брандо (Альтернативный)",
        "ability": "Остановка времени на 5 секунд",
        "stats": {"power": "A", "speed": "A", "range": "C", "durability": "B", "precision": "B", "potential": "A"},
        "quote": "«ZA WARUDO! Токе wo томарэ!»"
    },
    "Стенд Альт. Джонни": {
        "user": "Джонни Джостар (Альтернативный)",
        "ability": "Улучшенная версия Tusk с новыми актами",
        "stats": {"power": "A", "speed": "A", "range": "B", "durability": "B", "precision": "A", "potential": "A"},
        "quote": "«Бесконечное вращение!»"
    },
    "Стенд Альт. Хот Панц": {
        "user": "Хот Панц (Альтернативная)",
        "ability": "Улучшенный контроль плоти и создание жизни",
        "stats": {"power": "B", "speed": "A", "range": "C", "durability": "B", "precision": "A", "potential": "A"},
        "quote": "«Совершенная красота!»"
    }
    # ... остальные стенды оставь как были, долбоёб
}

# 🚀 Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """
🌀 *STAND ROULETTE - Steel Ball Run Edition* 🌀

*Добро пожаловать в мир стендов!* 
Здесь ты можешь получить случайный стенд из вселенной Steel Ball Run!

✨ *Доступные команды:*
/start - Показать это сообщение
/help - Правила и инструкции
/random stand - Получить случайный стенд (ОДНАЖДЫ!)
/My stand - Посмотреть свой текущий стенд

*Для Владельцев/Админов в группах:*
/Your stand @username - Посмотреть стенд другого игрока
/Your random stand @username - Выдать стенд игроку (админы)

*«Стенд - это воплощение твоего боевого духа!»* 💥
    """
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

# ❓ Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """
🎯 *ПРАВИЛА STAND ROULETTE* 🎯

*• Каждый пользователь может получить только ОДИН стенд!*
*• Выбор случаен и не может быть изменен!*
*• Судьба решит, какой стенд тебе достанется!*

⚡ *КОМАНДЫ:*
*/random stand* - Крутить рулетку стендов (ОДИН РАЗ!)
*/My stand* - Посмотреть свой стенд
*/Your stand @username* - Посмотреть чужой стенд (для админов)
*/Your random stand @username* - Выдать стенд игроку (для админов)

🌀 *О СТЕНДАХ:*
Стенды из вселенной Steel Ball Run обладают уникальными способностями, связанными с вращением, природными явлениями и парадоксами!

*«Воля определяет силу стенда!»* 🌪️
    """
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

# 🎰 Команда /random stand
@bot.message_handler(commands=['random'])
def random_stand(message):
    if message.text != "/random stand":
        bot.send_message(message.chat.id, "❌ Используй: /random stand", parse_mode="Markdown")
        return

    user_id = message.from_user.id

    # Проверка для @Nonae247 - может крутить сколько впадлу
    if user_id != 247 and user_id in user_stands:  # ЗАМЕНИ 247 НА НАСТОЯЩИЙ ID @Nonae247
        bot.send_message(message.chat.id, "⚠️ *У тебя уже есть стенд!*\nТы можешь получить только один стенд навсегда!", parse_mode="Markdown")
        return

    # Выбираем случайный стенд
    stand_name, stand_data = random.choice(list(STANDS.items()))

    # Сохраняем стенд пользователя
    user_stands[user_id] = {
        'stand_name': stand_name,
        'user_name': message.from_user.first_name,
        'username': message.from_user.username,
        'obtained_date': time.strftime("%d.%m.%Y %H:%M"),
        'stand_data': stand_data
    }

    # Отправляем крутое сообщение о получении стенда
    stand_text = f"""
🌀 *СТЕНД ПОЛУЧЕН!* 🌪️

⚡ *ТВОЙ СТЕНД:* *{stand_name}*
👤 *ПОЛЬЗОВАТЕЛЬ:* {stand_data['user']}

💥 *СПОСОБНОСТЬ:*
{stand_data['ability']}

📊 *ХАРАКТЕРИСТИКИ:*
• Сила: {stand_data['stats']['power']}
• Скорость: {stand_data['stats']['speed']} 
• Дальность: {stand_data['stats']['range']}
• Выносливость: {stand_data['stats']['durability']}
• Точность: {stand_data['stats']['precision']}
• Потенциал: {stand_data['stats']['potential']}

🗣️ *ФРАЗА:* {stand_data['quote']}

*«Этот стенд отражает твою душу!»* ✨
*Дата получения: {user_stands[user_id]['obtained_date']}*
    """

    bot.send_message(message.chat.id, stand_text, parse_mode="Markdown")

# 👤 Команда /My stand
@bot.message_handler(commands=['My'])
def my_stand(message):
    if message.text != "/My stand":
        bot.send_message(message.chat.id, "❌ Используй: /My stand", parse_mode="Markdown")
        return

    user_id = message.from_user.id

    if user_id not in user_stands:
        bot.send_message(message.chat.id, "❌ *У тебя еще нет стенда!*\nИспользуй /random stand чтобы получить свой стенд!", parse_mode="Markdown")
        return

    stand_info = user_stands[user_id]
    stand_data = stand_info['stand_data']

    stand_text = f"""
🌀 *ТВОЙ СТЕНД* 🌀

⚡ *ИМЯ:* *{stand_info['stand_name']}*
👤 *ОРИГИНАЛЬНЫЙ ПОЛЬЗОВАТЕЛЬ:* {stand_data['user']}

💥 *СПОСОБНОСТЬ:*
{stand_data['ability']}

📊 *ХАРАКТЕРИСТИКИ:*
• Сила: {stand_data['stats']['power']}
• Скорость: {stand_data['stats']['speed']} 
• Дальность: {stand_data['stats']['range']}
• Выносливость: {stand_data['stats']['durability']}
• Точность: {stand_data['stats']['precision']}
• Потенциал: {stand_data['stats']['potential']}

🗣️ *ФИРМЕННАЯ ФРАЗА:* 
{stand_data['quote']}

*«Этот стенд - твое воплощение воли!»* 💪
*Получен: {stand_info['obtained_date']}*
    """

    bot.send_message(message.chat.id, stand_text, parse_mode="Markdown")

# 👁️ Команда /Your stand (для админов)
@bot.message_handler(commands=['Your'])
def your_stand(message):
    user_id = message.from_user.id

    # Проверяем права - либо админ в группе, либо ID в списке ADMIN_IDS
    is_admin = False
    if message.chat.type != 'private':
        try:
            chat_member = bot.get_chat_member(message.chat.id, user_id)
            if chat_member.status in ['creator', 'administrator']:
                is_admin = True
        except:
            pass

    if user_id not in ADMIN_IDS and not is_admin:
        bot.send_message(message.chat.id, "⛔ *Только админы могут использовать эту команду!*", parse_mode="Markdown")
        return

    # Обработка /Your stand @username
    if message.text.startswith("/Your stand @"):
        username = message.text.split('@')[1].strip()

        # Ищем пользователя по username
        target_user_id = None
        for uid, stand_info in user_stands.items():
            if stand_info.get('username') and stand_info['username'].lower() == username.lower():
                target_user_id = uid
                break

        if not target_user_id:
            bot.send_message(message.chat.id, f"❌ *Стенд не найден!*\nПользователь @{username} еще не получил стенд!", parse_mode="Markdown")
            return

        stand_info = user_stands[target_user_id]
        stand_data = stand_info['stand_data']

        stand_text = f"""
🔍 *СТЕНД ПОЛЬЗОВАТЕЛЯ* @{username}

⚡ *СТЕНД:* *{stand_info['stand_name']}*
👤 *ВЛАДЕЛЕЦ:* {stand_info['user_name']}
🎭 *ОРИГИНАЛЬНЫЙ ПОЛЬЗОВАТЕЛЬ:* {stand_data['user']}

💥 *СПОСОБНОСТЬ:*
{stand_data['ability']}

📊 *ХАРАКТЕРИСТИКИ:*
• Сила: {stand_data['stats']['power']}
• Скорость: {stand_data['stats']['speed']} 
• Дальность: {stand_data['stats']['range']}
• Выносливость: {stand_data['stats']['durability']}
• Точность: {stand_data['stats']['precision']}
• Потенциал: {stand_data['stats']['potential']}

*Получен: {stand_info['obtained_date']}*
        """

        bot.send_message(message.chat.id, stand_text, parse_mode="Markdown")

    # Обработка /Your random stand @username
    elif message.text.startswith("/Your random stand @"):
        username = message.text.split('@')[1].strip()

        # Ищем пользователя по username (для этого нужно сначала получить его ID)
        # Это сложная хуйня, поэтому проще сделать через ответ на сообщение
        bot.send_message(message.chat.id, "❌ *Используй ответ на сообщение пользователя!*\nОтветь на сообщение нужного игрока и используй /Your random stand", parse_mode="Markdown")

    else:
        bot.send_message(message.chat.id, "❌ Используй: /Your stand @username или /Your random stand @username", parse_mode="Markdown")

# 🎲 Команда /Your random stand через reply
@bot.message_handler(commands=['Your_random'])
def your_random_stand(message):
    user_id = message.from_user.id

    # Проверяем права
    is_admin = False
    if message.chat.type != 'private':
        try:
            chat_member = bot.get_chat_member(message.chat.id, user_id)
            if chat_member.status in ['creator', 'administrator']:
                is_admin = True
        except:
            pass

    if user_id not in ADMIN_IDS and not is_admin:
        bot.send_message(message.chat.id, "⛔ *Только админы могут использовать эту команду!*", parse_mode="Markdown")
        return

    if not message.reply_to_message:
        bot.send_message(message.chat.id, "❌ *Ответь на сообщение пользователя!*\nЧтобы выдать стенд, ответь на сообщение нужного игрока", parse_mode="Markdown")
        return

    target_user_id = message.reply_to_message.from_user.id
    target_username = message.reply_to_message.from_user.username

    # Выбираем случайный стенд
    stand_name, stand_data = random.choice(list(STANDS.items()))

    # Сохраняем стенд пользователя
    user_stands[target_user_id] = {
        'stand_name': stand_name,
        'user_name': message.reply_to_message.from_user.first_name,
        'username': target_username,
        'obtained_date': time.strftime("%d.%m.%Y %H:%M"),
        'stand_data': stand_data
    }

    stand_text = f"""
🌀 *АДМИН ВЫДАЛ СТЕНД!* 🌪️

⚡ *СТЕНД:* *{stand_name}*
👤 *ДЛЯ ПОЛЬЗОВАТЕЛЯ:* @{target_username}
🎭 *ОРИГИНАЛЬНЫЙ ПОЛЬЗОВАТЕЛЬ:* {stand_data['user']}

💥 *СПОСОБНОСТЬ:*
{stand_data['ability']}

📊 *ХАРАКТЕРИСТИКИ:*
• Сила: {stand_data['stats']['power']}
• Скорость: {stand_data['stats']['speed']} 
• Дальность: {stand_data['stats']['range']}
• Выносливость: {stand_data['stats']['durability']}
• Точность: {stand_data['stats']['precision']}
• Потенциал: {stand_data['stats']['potential']}

🗣️ *ФРАЗА:* {stand_data['quote']}

*«Админ решил твою судьбу!»* 👑
*Выдан: {user_stands[target_user_id]['obtained_date']}*
    """

    bot.send_message(message.chat.id, stand_text, parse_mode="Markdown")

# ▶️ Запуск бота
print("🌀 Stand Roulette Bot запущен!")
print("⚡ Готов раздавать стенды!")
print("💥 Используй /start для начала")

try:
    bot.polling(none_stop=True, interval=1, timeout=30)
except Exception as e:
    print(f"❌ Ошибка: {e}")
    time.sleep(5)
    
