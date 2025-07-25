import telebot
from telebot import types
from telebot.types import LabeledPrice
import telegram
from utils.logger import setup_logger

logger = setup_logger()



def register_callback(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def call(c):
            parse = telegram.constants.ParseMode.HTML
            if c.data == 'rasklad':
                text = '🎴 <b>Расклад на Таро</b> — это возможность получить персональный ответ именно на твой вопрос или ситуацию.\nНе просто общие слова, а конкретные подсказки, которые помогут понять, что происходит внутри и вокруг, увидеть скрытые детали и сделать осознанный выбор.\n\n💰 Стоимость услуги — 100 рублей за один вопрос.\nПосле оплаты я внимательно сделаю расклад и объясню каждую карту — ты узнаешь то, что важно именно тебе.\n\nТы сможешь задать любой вопрос: про отношения, работу, личное развитие или любую ситуацию, которая волнует.\nЕсли хочешь, могу помочь сформулировать вопрос, чтобы расклад был максимально полезным.\n\n🌿 Атмосфера, мысли и полезности — в канале @rattarot89\n📩 Готов(а) — пиши и договоримся о деталях: @rattarolog'
                bot.send_message(c.message.chat.id, text, parse_mode=parse)
            if c.data == 'traktovka':
                text = '🔍 <b>Трактовка карт</b> — если ты сам(а) уже вытянул(а) карты, но не до конца понимаешь, что они хотят сказать.\nЯ помогу тебе разобрать каждый символ и рассказать, как это может относиться именно к твоей жизни.\n\n💡 Это не просто перевод значений, а живое понимание, которое помогает получить инсайты и лучше понять карты.\n\n💰 Стоимость — 150 рублей за трактовку одного расклада.\n\nЕсли есть свои карты и вопросы — пиши, расскажу, как это будет работать.\n\n🌿 Атмосфера, мысли и полезности — в канале @rattarot89\n📩 Для связи и заказа: @rattarolog'
                bot.send_message(c.message.chat.id, text, parse_mode=parse)
            if c.data == 'razbor':
                text = '🧬 <b>Разбор матрицы судьбы</b> — если хочется понять себя глубже.\nЭто про твои внутренние настройки: характер, сильные и слабые стороны, кармические задачи, таланты, отношения с людьми и собой.\n\nМатрица строится по дате рождения — и часто даёт очень точные инсайты:\nпочему одни и те же ситуации повторяются, где твоя сила, а где — точка роста.\n\n💰 Стоимость разбора — 350 рублей.\nВ ответ ты получишь голосовое или текстовое сообщение с подробным объяснением и опорой именно на твою дату.\n\n🌿 Атмосфера, мысли и полезности — в канале @rattarot89\n📩 Хочешь узнать, что в твоей матрице? Пиши: @rattarolog'
                bot.send_message(c.message.chat.id, text, parse_mode=parse)
            if c.data == 'guides':
                text = '📚 <b>Гайды, составленные нашими экспертами</b> — если хочешь разобраться в теме самостоятельно, но без воды и хаоса из интернета.\n\nРазовые, по делу. Удобно сохранить и возвращаться.\n\nЧтобы посмотреть доступные гайды, напиши команду:\n/guide'
                bot.send_message(c.message.chat.id, text, parse_mode=parse)
            if c.data == 'matriza':
                try:
                    amount = 650
                    title = "🧬МАТРИЦА🧬"
                    url = bot.create_invoice_link(
                            title=title,
                            description="🧬МАТРИЦА🧬 - Лучший гайд по разбору матрицы",
                            currency="XTR",
                            prices=[LabeledPrice(label="XTR", amount=amount)],
                            payload="MATRIZA",
                            provider_token=None
                        )
                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("КУПИТЬ ГАЙД 🧬МАТРИЦА🧬", url=url)
                    markup.add(button)
                    text = '🧬 <b>Как разбирать матрицу судьбы самостоятельно</b>\nЭтот гайд — для тех, кто хочет не просто смотреть на красивые схемы, <b>а разбираться в себе и людях через матрицу.</b>\nТы узнаешь, что значат основные позиции, как считывать смысл за цифрами, и что с этим делать в реальности.\nПодойдёт и новичкам, и тем, кто уже делал разборы, и как база, если хочешь начать помогать другим и <b>зарабатывать на разборе кодов</b>'
                    bot.send_message(c.message.chat.id, text, reply_markup=markup, parse_mode=parse)
                    logger.info(f'Пользователь {c.message.chat.id} выбрал курс МАТРИЦА')
                except Exception as e:
                    text = '❗️Что-то пошло не так.\nИногда техника чудит — давай попробуем ещё раз чуть позже.\n\nЕсли ошибка повторяется или совсем непонятно, что происходит — напиши мне, разберёмся: @lillbreathyy\n\nСпасибо за терпение 💫'
                    logger.error(f'У пользователя {c.message.chat.id} произошла ошибка при формировании ссылки оплаты курса МАТРИЦА: {e}', exc_info=True)
                    bot.send_message(c.message.chat.id, text)
            if c.data == 'finkod':
                try:
                    amount = 450
                    title = '💸ФИНАНСОВЫЙ КОД💸'
                    url = bot.create_invoice_link(
                        title=title,
                        description="💸ФИНАНСОВЫЙ КОД💸 - Лучший гайд по финансовому коду",
                        currency="XTR",
                        prices=[LabeledPrice(label="XTR", amount=amount)],
                        payload="FINKOD",
                        provider_token=None
                    )
                    markup = types.InlineKeyboardMarkup()
                    button = types.InlineKeyboardButton("КУПИТЬ ГАЙД 💸ФИНАНСОВЫЙ КОД💸", url=url)
                    markup.add(button)
                    text = '💸 <b>Финансовый код</b>\nГайд для тех, кто хочет понять, <b>почему с деньгами не складывается</b> — и как это связано с твоими числами по дате рождения.\nРасскажу, <b>какие энергии отвечают за финансы</b>, как они могут «зависать» и что с этим делать.'
                    bot.send_message(c.message.chat.id, text, reply_markup=markup, parse_mode=parse)
                    logger.info(f'Пользователь {c.message.chat.id} выбрал курс ФИНКОД')
                except Exception as e:
                    text = '❗️Что-то пошло не так.\nИногда техника чудит — давай попробуем ещё раз чуть позже.\n\nЕсли ошибка повторяется или совсем непонятно, что происходит — напиши мне, разберёмся: @lillbreathyy\n\nСпасибо за терпение 💫'
                    logger.error(
                        f'У пользователя {c.message.chat.id} произошла ошибка при формировании ссылки оплаты курса ФИНКОД: {e}',
                        exc_info=True)
                    bot.send_message(c.message.chat.id, text)
