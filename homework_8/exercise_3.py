""" 3. Откройте файл «unsorted_names.txt» содержащий имена студентов.
Прочитайте данные, отсортируйте их и запишите в новый файл «sorted_names.txt» (каждое имя начинается с новой строки
_______
Aaron
Adrian
…..
Wiley
________
 """

with open('unsorted_name.txt', 'r') as file:
    name = file.readlines()
    sorted_file = sorted(name)
with open('sorted_names.txt', 'w') as file:
    file.writelines(sorted_file)