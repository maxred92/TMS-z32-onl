""" 2. Создать скрипт который получает от пользователя 4 строки с данными (данные произвольные)
Создать файл и записать в него первые 2 строки (после данной операции закрыть файл)
Преобразовать оставшиеся 2 строки в строки в верхнем регистре и добавить их в созданный файл
В итоговом файле должно быть 4 строки каждая из которых оканчивается символом « | » и начинается с новой строки
 """

a = input("enter word: ")
b = input("enter word: ")
c = input("enter word: ")
d = input("enter word: ")

with open('exercise_2.txt', 'w') as file:
    lines = [a,b]
    for  line in lines:
        file.write(line + '\n')
with open('exercise_2.txt', 'a') as file:
    lines = [c,d]
    for  line in lines:
        file.write(line.upper() + '\n')
with open('exercise_2.txt', mode = 'w') as file:
    lines = [a,b,c,d]
    for  line in lines:
        file.write(line + '|\n')