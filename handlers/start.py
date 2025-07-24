import telebot
from telebot import types
from telebot.types import LabeledPrice
import telegram
from utils.logger import setup_logger

logger = setup_logger()



def register_handlers(bot, users):
    @bot.message_handler(commands=['start'])
    def start(mess):
        try:
            source = mess.text.split(' ')[1] if len(mess.text.split()) > 1 else 'direct'
            print(source)
            tg_id = mess.chat.id
            username = mess.from_user.username or 'unknown'
            name = mess.from_user.first_name
            users.new(name, username, tg_id, source)
            logger.info(f'Пользователь {tg_id} нажал старт')

            parse = telegram.constants.ParseMode.HTML
            markup = types.InlineKeyboardMarkup(row_width=2)
            rasklad = types.InlineKeyboardButton('✨РАСКЛАД✨', callback_data='rasklad')
            traktovka = types.InlineKeyboardButton('🃏ТРАКТОВКА🃏', callback_data='traktovka')
            razbor = types.InlineKeyboardButton('🌌РАЗБОР🌌', callback_data='razbor')
            guides = types.InlineKeyboardButton('📚ГАЙДЫ📚', callback_data='guides')
            markup.add(rasklad, traktovka, razbor, guides)
            text = ' Привет!👋\nХорошо, что ты тут. Иногда достаточно просто задать вопрос — и становится чуть понятнее, куда двигаться дальше.\n\nЗдесь ты можешь:\n— Получить <b>расклад на Таро</b> — честный, без шаблонов, с акцентом на тебя\n— <b>Разобраться в значениях карт</b>, если сам(а) что-то вытянул(а)\n— Запросить <b>разбор матрицы судьбы</b> — чтобы лучше понять себя, свои сильные и слабые стороны\n— Приобрести различные <b>гайды</b>, которые помогут тебе улучшить свои навыки\n\n✨ Всё с вниманием к тебе!\nЖми на нужный пункт ниже — и начнём👇'
            bot.send_message(mess.chat.id, text, reply_markup=markup, parse_mode=parse)
        except Exception as e:
            text = '❗️Что-то пошло не так.\nИногда техника чудит — давай попробуем ещё раз чуть позже.\n\nЕсли ошибка повторяется или совсем непонятно, что происходит — напиши мне, разберёмся: @lillbreathyy\n\nСпасибо за терпение 💫'
            logger.error(
                f'У пользователя {mess.chat.id} произошла ошибка в команде старт: {e}',
                exc_info=True)
            bot.send_message(mess.chat.id, text)

