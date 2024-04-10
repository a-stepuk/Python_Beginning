# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
#
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
#
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

vowel_letters = {'а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё'}
vowel_counter = 0
vowel_counter_set = set()

fraza_list = stroka.split()

if len(fraza_list) < 2:
    print("Количество фраз должно быть больше одной!")
    exit()

for i in range(len(fraza_list)):
    for char in fraza_list[i]:
        if char in vowel_letters:
            vowel_counter += 1

    vowel_counter_set.add(vowel_counter)
    vowel_counter = 0

if len(vowel_counter_set) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
