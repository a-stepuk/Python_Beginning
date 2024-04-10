data = [x + 10 for x in range(10)]
res = set(filter(lambda x: x % 2 == 0, data))
print(data)
print(res) # [0, 2, 4, 6, 8]
