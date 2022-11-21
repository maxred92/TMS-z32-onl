str = str(input('Enter the string: '))
str_low = str.lower()
dict = {i: str_low.count(i) for i in str_low}
print(dict)