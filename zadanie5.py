"""
Proszę policzyć liczbę produktów sprzedanych w weekendy (https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday).
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> zad_5
    9983
    >>> lista_test = ['order_id,product_name,pieces_sold,price_per_item,order_date,shop_id','1,a,1,1,2021-10-24,shop_1','1,a,2,1,2021-10-23,shop_1','1,a,2,1,2021-10-25,shop_1','1,a,'',1,2021-10-23,shop_1']
    >>> product_sold_weekend(lista_test)
    4
"""

from otwarcie import czytanie
from datetime import datetime

baza = czytanie()

def product_sold_weekend(lista: list) -> int:
    lista = lista[1:]
    product_count = 0
    for a in lista:
        line_list = a.split(',')
        order_date = line_list[4]
        pieces_sold = line_list[2]

        date = datetime.fromisoformat(order_date)
        if date.weekday() in (5, 6):
            if(not pieces_sold.isnumeric()):
                pieces_sold = 1
            product_count += int(pieces_sold)

    return product_count

zad_5 = product_sold_weekend(baza)




