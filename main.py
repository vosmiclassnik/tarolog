import telebot
from config import api
from handlers import start, guides, callback_handler
from payments import stars_pay
from database.users import users
from database.payments import payments
from database.orders import orders
bot = telebot.TeleBot(api)



#базы данных
payments = payments('pay')
users = users('users')
orders = orders('orders')
payments.create_db()
users.create_db()
orders.create_db()




#обработчики команд
callback_handler.register_callback(bot)
start.register_handlers(bot, users)
guides.register_handlers(bot, orders)
stars_pay.register_payment(bot, payments)
bot.infinity_polling()