from pathlib import Path

FILE = 'MOCK_DATA.csv'
p = Path(FILE)

def czytanie():
    lista = []
    with open(p, 'r') as file:
        for line in file:
            if '"' not in line:
                lista.append(line.strip())
    return lista