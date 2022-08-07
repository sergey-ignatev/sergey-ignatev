from db_work.db import insert_google_table, select_db_table, delete_row_db


def data_logic(new_values: tuple, quote: float):
    """
    Функция синхронизирует данные в БД с гугл таблицей.
    :param new_values: текущая версия гугл таблицы
    :param quote: текущие котировки ЦБ
    :return: функция ничего не возвращает
    """
    set_table = set(select_db_table())
    set_new_values = set(new_values)
    create = set_new_values - set_table
    delete = set_table - set_new_values

    for de in delete:
        delete_row_db(de[0])

    for cr in create:
        rub = float(cr[2]) * quote
        insert_google_table(cr[0], cr[1], cr[2], cr[3], rub)
        # print('%s, %s, %s' % (cr[0], cr[3], rub))
