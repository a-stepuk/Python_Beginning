# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

#n = 385916
n = 123322

n_as_string = str(n)

# part1 = 0
# part2 = 0
#
# count = 0
#
# for digit in n_as_string:
#     if count <= 2:
#         part1 += int(digit)
#     else:
#         part2 += int(digit)
#
#     count += 1

part1 = int(n_as_string[0]) + int(n_as_string[1]) + int(n_as_string[2])
part2 = int(n_as_string[3]) + int(n_as_string[4]) + int(n_as_string[5])

if part1 == part2:
    print("yes")
else:
    print("no")
