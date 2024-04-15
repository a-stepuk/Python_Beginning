# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd


# Функция, переводящая список в one hot вид:
def my_dummies(datalist):
    who_am_i = datalist[0]

    for i in range(len(datalist)):
        if datalist[i] == who_am_i:
            datalist[i] = 0
        else:
            datalist[i] = 1


lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

print(lst)

# Вызов функции, переводящей список в one hot вид:
my_dummies(lst)

data = pd.DataFrame({'whoAmI': lst})

print(lst)
