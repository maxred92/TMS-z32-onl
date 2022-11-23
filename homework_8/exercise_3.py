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
    full_txt = sorted(file.read().splitlines())
    print(full_txt)
with open('sorted_names.txt', 'w') as file:
    for item in full_txt:
        file.write(item + "\n")
    print(full_txt, file=file)