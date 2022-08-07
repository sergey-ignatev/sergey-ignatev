from datetime import datetime

from requests_html import HTMLSession
import xml.etree.ElementTree as ET

date_now = datetime.now().strftime("%d/%m/%Y")

http = HTMLSession()
url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_now}'


def get_value_rub() -> float:
    """
    Получение курса рубля на момент запроса
    :return: курс рубля
    """
    response = http.get(url, timeout=2)
    tree = ET.fromstring(response.text)
    return float(tree.findall('Valute')[10][4].text.replace(",", "."))
