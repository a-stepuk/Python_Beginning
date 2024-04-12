'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

# Задача 38:
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    last_name = "Иванов"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def write_list_to_file(file_name, list):
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(list)


def delete_file(file_name, lst):
    res = read_file(file_name)
    res_size = len(res)

    count = 0
    del_counter = res_size

    while del_counter > 0 and count < del_counter:
        if res[count]["Имя"] == str(lst[0]) and res[count]["Телефон"] == str(lst[2]):
            res.remove(res[count])
            del_counter -= 1
        else:
            count += 1

    if len(res) == 0:
        print("Удалены все записи.")
    elif res_size == len(res):
        print("По данному имени и телефону не обнаружено ни одной записи.")
        return

    write_list_to_file(file_name, res)

    if len(res) > 0:
        print(f"Удалено {res_size - del_counter} записей.")


def update_file(file_name, data_to_update):
    res = read_file(file_name)
    new_data = []
    updated_rows_counter = 0

    for el in res:
        if el["Имя"] == str(data_to_update[0]) and el["Телефон"] == str(data_to_update[2]):
            if len(new_data) == 0:
                print("Найдена(ы) запись(и), соответствующая(ие) критериям поиска. Введите новые данные для внесения изменений:")
                new_data = get_info()

            el["Имя"] = new_data[0]
            el["Фамилия"] = new_data[1]
            el["Телефон"] = new_data[2]

            updated_rows_counter += 1

    write_list_to_file(file_name, res)

    if updated_rows_counter == 0:
        print("Не найдена ни одна запись, соответствующая критериям поиска.")
    else:
        print(f"Обновлены данные в {updated_rows_counter} записях.")


file_name = 'phone.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print("Файл отсутствует. Нечего удалять")
                continue
            delete_file(file_name, get_info())
        elif command == 'u':
            if not exists(file_name):
                print("Файл отсутствует. Негде изменять данные")
                continue
            update_file(file_name, get_info())


main()
