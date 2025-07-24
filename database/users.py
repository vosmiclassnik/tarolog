import sqlalchemy as db
import datetime
from utils.logger import setup_logger

logger = setup_logger()





class users:
    def __init__(self, name):
        self.users = name
    def create_db(self):
        global conn
        engine = db.create_engine(f'sqlite:///{self.users}.db')
        conn = engine.connect()
        meta = db.MetaData()
        self.users = db.Table('users', meta,
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('username', db.Text),
                         db.Column('name', db.Text),
                         db.Column('created_at', db.DateTime),
                         db.Column('source', db.Text),
                         db.Column('tg_id', db.Integer)
                         )
        meta.create_all(engine)

    def new(self, name, username, tg_id, source):
        try:
            select = db.select(self.users).where(self.users.columns.tg_id==tg_id)
            res = conn.execute(select).fetchone()
            if res is None:
                insert_query = self.users.insert().values([
                    {'name': name, 'username': username, 'tg_id': tg_id, 'created_at': datetime.datetime.now(), 'source' : source}
                ])
                conn.execute(insert_query)
                conn.commit()
        except Exception as e:
            logger.error(f'(new)В базе данных users произошла ошибка: {e}', exc_info=True)


    # тестовые

    def test_output(self):
        select = db.select(self.users)
        res = conn.execute(select)
        output = res.fetchall()
        print(output)
        return output
    def delete_user(self, name):
        del_q = db.delete(self.users).where(self.users.columns.user_name == name)
        conn.execute(del_q)
        conn.commit()
    def delete_all(self):
        del_q = db.delete(self.users)
        conn.execute(del_q)
        conn.commit()










