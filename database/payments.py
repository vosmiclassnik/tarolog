import sqlalchemy as db
import datetime
from utils.logger import setup_logger

logger = setup_logger()


class payments:
    def __init__(self, name):
        self.pay = name
    def create_db(self):
        global conn
        engine = db.create_engine(f'sqlite:///{self.pay}.db')
        conn = engine.connect()
        meta = db.MetaData()
        self.pay = db.Table('payments', meta,
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('amount', db.Integer),
                         db.Column('product', db.Text),
                         db.Column('status', db.Text),
                         db.Column('username', db.Text),
                         db.Column('created_at', db.DateTime),
                         db.Column('tg_id', db.Integer)
                         )
        meta.create_all(engine)

    def new(self, amount, username, tg_id, status, product):
        try:
            insert_query = self.pay.insert().values([
                {'amount': amount, 'username': username, 'tg_id': tg_id, 'created_at': datetime.datetime.now(), 'status': status, 'product' : product}
            ])
            conn.execute(insert_query)
            conn.commit()
        except Exception as e:
            logger.error(f'(new)В базе данных payments произошла ошибка: {e}', exc_info=True)


#тестовые
    def test_output(self):
        select = db.select(self.pay)
        res = conn.execute(select)
        output = res.fetchall()
        print(output)
        return output
    def delete_user(self, name):
        del_q = db.delete(self.pay).where(self.pay.columns.user_name == name)
        conn.execute(del_q)
        conn.commit()
    def delete_all(self):
        del_q = db.delete(self.pay)
        conn.execute(del_q)
        conn.commit()
