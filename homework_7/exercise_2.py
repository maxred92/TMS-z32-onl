texts = input('Enter words through space: ')
print('List of palindromes: ',tuple(filter(lambda x: (x == "".join(reversed(x))), texts.split()))) 
