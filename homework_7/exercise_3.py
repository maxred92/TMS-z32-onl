
""" Решение задачи с помощью функции map()
 
n = int(input('enter number: '))
squared = list(map(lambda i: i** 2, range(1, n + 1)))
print (squared)
         """



def square(n):
    for i in range (1,n+1):
        print ("number: ",i,"square number: ", i**2)
square(int(input("enter number: ")))


