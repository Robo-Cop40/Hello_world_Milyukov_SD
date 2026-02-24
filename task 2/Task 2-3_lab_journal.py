name = input('Введите ФИО исследователя: ')
date = input('Введите дату: ')
name_of_exp = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')

with open ('journal.txt', 'w', encoding="utf-8") as journal:
    journal.write("+--------------------------------------------------+\n")
    journal.write("|          Электронный лабораторный журнал         |\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write(f"| ФИО исследователя : {name}\n")
    journal.write(f"| Дата : {date}\n")
    journal.write(f"| Эксперимент : {name_of_exp}\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write(f"| Вывод: {conclusion}\n")
    journal.write("+--------------------------------------------------+\n")

print("Файл 'journal.txt' создан!")