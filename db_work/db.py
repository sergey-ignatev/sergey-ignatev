import os

import sqlalchemy as sa

metadata = sa.MetaData()
connection = {'user': f'{os.environ.get("POSTGRES_USER")}', 'database': f'{os.environ.get("POSTGRES_DB")}',
              'host': f'{os.environ.get("DATABASE_HOST")}', 'password': f'{os.environ.get("POSTGRES_PASSWORD")}'}
dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**connection)
engine = sa.create_engine(dsn)
connect_db = engine.connect()

google_table = sa.Table(
    'table_update', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('order_id', sa.Integer),
    sa.Column('cost_usd', sa.Integer),
    sa.Column('delivery_date', sa.Date),
    sa.Column('cost_rub', sa.Integer),
)


def insert_google_table(row1, row2, row3, row4, cost_rub):
    """
    Функция записывает строку в таблицу
    :param row1:
    :param row2:
    :param row3:
    :param row4:
    :param cost_rub: цена в рублях
    :return:
    """
    connect_db.execute(google_table.insert().values(
        id=row1,
        order_id=row2,
        cost_usd=row3,
        delivery_date=row4,
        cost_rub=cost_rub
    ))


def select_db_table() -> tuple:
    """
    Получает все данные из таблицы БД
    """
    return connect_db.execute("SELECT id, order_id, cost_usd, delivery_date FROM table_update;")


def delete_row_db(row):
    """
    Удаляет выбранную строку из таблицы в БД
    :param row: ID строки для удаления
    :return:
    """
    return connect_db.execute(google_table.delete().where(google_table.c.id == f"{row}"))


if __name__ == '__main__':
    engine = sa.create_engine(dsn)
    metadata.create_all(engine)
