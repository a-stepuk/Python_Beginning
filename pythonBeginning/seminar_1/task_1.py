# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = 721

digit_1 = n // 100
digit_2 = (n % 100) // 10
digit_3 = n % 10

res = digit_1 + digit_2 + digit_3

print(res)
