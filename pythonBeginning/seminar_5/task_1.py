# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

def f(a, b):
    result = a

    if b == 1:
        return result

    return result * f(result, b - 1)

a = 5
b = 3
print(f(a, b))
