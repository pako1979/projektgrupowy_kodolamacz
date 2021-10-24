"""
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> zad_2['Coffee - Egg Nog Capuccino']
    1060.7

    >>> zad_2['Muffin - Blueberry Individual']
    74053.54
"""




from pathlib import Path
FILE = r'C:\Users\Lenovo\Downloads\MOCK_DATA.csv'
p = Path(FILE)

def czytanie(p):
    lista = []
    with open(p, 'r') as file:
        for line in file:
            if '"' not in line:
                lista.append(line.strip().split(','))
    return lista

def total_buy_cost(FILE):
    features = czytanie(FILE)
    dict = {}
    for feature in features:
        product_name = feature[1]
        pieces_sold = 1 if not feature[2] else int(feature[2])
        price_per_item = float(feature[3])
        dict[product_name] = round(pieces_sold * price_per_item,2)
    return dict

zad_2 = total_buy_cost(FILE)
