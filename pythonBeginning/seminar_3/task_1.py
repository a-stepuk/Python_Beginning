# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

list_1 = [1, 2, 3, 4, 5, 3, 3]
k = 3

counter = 0

for i in list_1:
    if i == k:
        counter += 1

print(counter)
