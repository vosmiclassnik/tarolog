import telebot
from telebot import types
from telebot.types import LabeledPrice
from utils.logger import setup_logger

logger = setup_logger()
def register_payment(bot, payments):
    @bot.pre_checkout_query_handler(func=lambda query: True)
    def checkout(pre_checkout_query):
        bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                      error_message="Что-то пошло не так..\n\nУже все чиним!")

    @bot.message_handler(content_types=['successful_payment'])
    def success(mess):
        if mess.successful_payment.invoice_payload == "MATRIZA":
            try:
                bot.refund_star_payment(mess.chat.id, mess.successful_payment.telegram_payment_charge_id)
                text = 'Спасибо за покупку! 💫\nНадеюсь, гайд даст тебе не просто информацию, а настоящие инсайты — про себя, свои сценарии и точки роста.\n\nЕсли что-то захочется обсудить или уточнить — всегда можно написать: @lillbreathyy\n\nПусть знания пойдут в дело 🌿'
                bot.send_message(mess.chat.id, text)
                with open("pay.db", "rb") as f:  # ← путь к файлу
                    bot.send_document(mess.chat.id, f)
                username = mess.from_user.username
                tg_id = mess.from_user.id
                product = mess.successful_payment.invoice_payload
                amount = mess.successful_payment.total_amount
                payments.new(amount=amount, username=username, tg_id=tg_id, status='success', product=product)
                logger.info(f'Пользователь {tg_id} успешно оплатил продукт {product}. Юзернейм для обращения: {username}')
            except Exception as e:
                text = '❗️Что-то пошло не так.\nИногда техника чудит — давай попробуем ещё раз чуть позже.\n\nЕсли ошибка повторяется или совсем непонятно, что происходит — напиши мне, разберёмся: @lillbreathyy\n\nСпасибо за терпение 💫'
                logger.error(
                    f'У пользователя {mess.chat.id} произошла ошибка при выдачи курса МАТРИЦА: {e}',
                    exc_info=True)
                payments.new(amount=amount, username=username, tg_id=tg_id, status='success', product=product)
                bot.send_message(mess.chat.id, text)
        if mess.successful_payment.invoice_payload =='FINKOD':
            try:
                bot.refund_star_payment(mess.chat.id, mess.successful_payment.telegram_payment_charge_id)
                text = 'Спасибо за покупку! 💫\nНадеюсь, гайд даст тебе не просто информацию, а настоящие инсайты — про себя, свои сценарии и точки роста.\n\nЕсли что-то захочется обсудить или уточнить — всегда можно написать: @lillbreathyy\n\nПусть знания пойдут в дело 🌿'
                bot.send_message(mess.chat.id, text)
                with open("orders.db", "rb") as f:  # ← путь к файлу
                    bot.send_document(mess.chat.id, f)
                username = mess.from_user.username
                tg_id = mess.from_user.id
                product = mess.successful_payment.invoice_payload
                amount = mess.successful_payment.total_amount
                payments.new(amount=amount, username=username, tg_id=tg_id, status='success', product=product)
                logger.info(f'Пользователь {tg_id} успешно оплатил продукт {product}. Юзернейм для обращения: {username}')
            except Exception as e:
                text = '❗️Что-то пошло не так.\nИногда техника чудит — давай попробуем ещё раз чуть позже.\n\nЕсли ошибка повторяется или совсем непонятно, что происходит — напиши мне, разберёмся: @lillbreathyy\n\nСпасибо за терпение 💫'
                logger.error(
                    f'У пользователя {mess.chat.id} произошла ошибка при выдачи курса ФИНКОД: {e}',
                    exc_info=True)
                payments.new(amount=amount, username=username, tg_id=tg_id, status='xyinya', product=product)
                bot.send_message(mess.chat.id, text)