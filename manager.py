from time import sleep

from external.cbr import get_value_rub
from external.google_api import google_parser
from core.engine import data_logic


def main():
    """
    Обновляет данные раз в минуту.
    :return: вечный цикл
    """
    while True:
        # quotes = get_value_rub()
        # data_logic(google_parser(), quotes)
        sleep(60)
        print('ping')


if __name__ == '__main__':
    main()
