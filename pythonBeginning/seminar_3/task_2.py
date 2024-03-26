# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 12, 6, 7, 8, 15, -5, 0]
k = -3

max = list_1[0]
diff = abs(k - max)

for i in range(1, len(list_1)):
    if list_1[i] == k:
        max = list_1[i]

        break
    elif diff > abs(k - list_1[i]):
        diff = abs(k - list_1[i])
        max = list_1[i]

print(max)
