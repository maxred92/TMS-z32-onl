a = input("enter words: ")
words = str.capitalize(a)
b = words.split()
c = b[-1]
last = str.capitalize(c)
print(' '.join(b[0:-1]),last)


