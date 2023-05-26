# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные **DONE**
# 2. Программа должна сохранять данные в текстовом файле **DONE**
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной **DONE**
# 5.Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных



# Созадние и добавление контактов
def open_file():
    num_of_counter = 0

    global name
    global surname
    global phone_number

    try:
        with open('PhoneGuide.txt', 'r') as book:
            num_of_counter = len(book.readlines())
        with open('PhoneGuide.txt', 'a', encoding='UTF-8') as book:
            name = str(input('Введите имя: '))
            surname = str(input('Введите фамилию: '))
            phone_number = str(input('Введите номер телефона: '))
            book.write(f'{num_of_counter + 1}. {name} {surname}: {phone_number}\n')
    except:
        with open('PhoneGuide.txt', 'a', encoding='UTF-8') as book:
            name = str(input('Введите имя: '))
            surname = str(input('Введите фамилию: '))
            phone_number = str(input('Введите номер телефона: '))
            book.write(f'{num_of_counter + 1}. {name} {surname}: {phone_number}\n')
    


# находим контакт
def find_contact():
        # Открываем файл
    with open('PhoneGuide.txt', 'r', encoding='UTF-8') as book:
        # Запрашиваем у пользователя информацию для поиска
        search_criteria = str(input("Введите характеристику для поиска: "))
        # Итерируемся по строкам файла
        for line in book:
            # Проверяем, содержит ли текущая строка информацию, искомую пользователем
            if search_criteria.lower() in line.lower():
                # Распечатываем строку, содержащую информацию пользователя
                print(line)
            else:
                print('Контакт не найден')


# изменяем данные контакта
def change_data():
    with open('PhoneGuide.txt', 'r', encoding='UTF-8') as book:
        lines = []
        search_criteria = str(input("Введите контакт который нужно найти и изменить: "))
        for line in book:
            lines.append(line)
            if search_criteria in line:
                print(line)
                new_information = str(input("Введите измененный текст: "))
                line = line.replace(search_criteria, new_information)
                lines[-1] = line

    # Перезаписываем файл с измененными данными
    with open('PhoneGuide.txt', 'w', encoding='UTF-8') as book:
        for line in lines:
            book.write(line)

def del_contact():
        # Открываем файл
    with open('PhoneGuide.txt', 'r', encoding='UTF-8') as book:
        # Создаем пустой список для хранения строк файла
        lines = []
        # Запрашиваем у пользователя информацию для поиска
        search_criteria = input("Введите характеристику для поиска: ")
        # Итерируемся по строкам файла и добавляем их в список
        for line in book:
            # Проверяем, содержит ли текущая строка информацию, искомую пользователем
            if search_criteria not in line:
                # Добавляем строку в список, если она не содержит искомую информацию
                lines.append(line)

    # Перезаписываем файл без удаленной строки
    with open('PhoneGuide.txt', 'w', encoding='UTF-8') as book:
        for line in lines:
            book.write(line)



# open_file()
# find_contact()
# change_data()
# del_contact()
