line = input("enter word")
s = input("enter symbol")
n = int(input("enter number"))
a = line[::2]
b = line[1::2]
c = a+s*n+b
print(line,c,n*'!',sep='\n')
