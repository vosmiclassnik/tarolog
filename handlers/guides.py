import telebot
import telegram
from telebot import types
from telebot.types import LabeledPrice
from utils.logger import setup_logger

logger = setup_logger()
parse = telegram.constants.ParseMode.HTML
def register_handlers(bot):
    @bot.message_handler(commands=['guide'])
    def guide(mess):
        markup = types.InlineKeyboardMarkup(row_width=2)
        matriza_curs = types.InlineKeyboardButton('🧬МАТРИЦА🧬', callback_data='matriza')
        finkod_curs = types.InlineKeyboardButton('💸ФИНКОД💸', callback_data='finkod')
        markup.add(matriza_curs, finkod_curs)

        text = '📚 Гайды по самопознанию — для тех, кто хочет понять себя глубже и работать с темами осознанно, без лишнего.\n\n💸 <b>Финансовый код в матрице судьбы</b>\nПочему деньги приходят (или нет)? Какой у тебя сценарий, и как его можно перепрошить?\n🧾 Формат: PDF\n💰 450 звёзд Telegram или 499₽ переводом\n\n🧬 <b>Как разбирать матрицу судьбы самостоятельно</b>\nГайд, который поможет читать матрицу — свою и чужую — без шаблонов и лишней мистики.\n🧾 Формат: PDF\n💰 650 звёзд Telegram или 699₽ переводом\n\n🌿 Атмосфера, мысли и полезности — в канале @rattarot89\n📩 Чтобы оплатить переводом или задать вопрос — пиши: @rattarolog\nОплата звездами ниже👇'
        bot.send_message(mess.chat.id, text, reply_markup=markup, parse_mode=parse)







