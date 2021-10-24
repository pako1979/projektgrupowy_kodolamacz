from otwarcie import czytanie
from datetime import datetime

db = czytanie()
list_db = []

# create new db with lists of items
for row in db[1:]:
    list_db.append(row.split(','))

# add sales from each record to specific quarter
def sumy_kwartalow(lista):
    Q1_sum = 0
    Q2_sum = 0
    Q3_sum = 0
    Q4_sum = 0

    for i in lista:
        quarter = (datetime.strptime(i[4], "%Y-%m-%d").month-1)//3
        if quarter == 0:
            if i[2] == '':
                Q1_sum += float(i[3])
            else:
                Q1_sum += float(i[2]) * float(i[3])
        elif quarter == 1:
            if i[2] == '':
                Q2_sum += float(i[3])
            else:
                Q2_sum += float(i[2]) * float(i[3])
        elif quarter == 2 :
            if i[2] == '':
                Q3_sum += float(i[3])
            else:
                Q3_sum += float(i[2]) * float(i[3])
        else:
            if i[2] == '':
                Q4_sum += float(i[3])
            else:
                Q4_sum += float(i[2]) * float(i[3])
    return tuple(Q1_sum, Q2_sum, Q3_sum, Q4_sum)
    # present sums for each quarter
    print(f'Sum of sales for Q1: {round(Q1_sum, 2)}')
    print(f'Sum of sales for Q1: {round(Q2_sum, 2)}')
    print(f'Sum of sales for Q1: {round(Q3_sum, 2)}')
    print(f'Sum of sales for Q1: {round(Q4_sum, 2)}')