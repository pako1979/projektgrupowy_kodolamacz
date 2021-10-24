"""
Proszę wczytać plik i wyświetlić pierwsze 10 nazw produktów posortowane w kolejności alfabetycznej.
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> zad_1  # doctest: +NORMALIZE_WHITESPACE
    ('Amaretto', 'Appetizer - Cheese Bites', 'Appetizer - Escargot Puff',
    'Appetizer - Shrimp Puff', 'Appetizer - Smoked Salmon / Dill', 'Appetizer - Southwestern', 'Appetizer - Veg
    Assortment', 'Apple - Custard', 'Apple - Granny Smith', 'Apple - Northern Spy')

    >>> len(zad_1)
    10
"""

from otwarcie import czytanie

baza = czytanie()

def get_all_product_list(lista: list) -> tuple:
    lista = lista[1:]
    products = []
    for a in lista:
        products.append(a.split(',')[1])

    # remove dups
    products = set(products)
    # sort
    products = sorted(products)
    # first 10
    return tuple(products[0:10])


zad_1 = get_all_product_list(baza)
