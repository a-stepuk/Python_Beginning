# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 1000

degree = 1
degree_counter = 0

while degree <= n:
    print(degree)

    degree_counter += 1
    degree = pow(2, degree_counter)
