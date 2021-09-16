import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "1983076539:AAHOTchr6v7BrRYW7XQoBne4iT6m0sKVVFs"  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)


# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"""Assalomu alaykum {username},  men sizga so'z va matnlarni Lotindan Krillga va Krilldan Lotinga o'girishga yordam beraman.  \n
Ассалому алайкум, мен сизга сўз ва матнларни Лотиндан Криллга ва Криллдан Лотинга ўгиришга ёрдам бераман. \n
(Kichik shart: lotin va krillda aralash yozilgan so'zlarni faqat lotinga o'giraman)"""
    xabar += '\nMatningizni yuboring.'
    chatid = message.chat.id
    bot.send_message(chatid, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()
