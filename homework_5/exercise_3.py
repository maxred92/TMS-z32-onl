import random
name = str(input('Hello! Enter your name: '))
number = input('Great, {0}, Enter number from 1 to 100 or stop for exit: '.format(name))
n = random.randint(1, 100)
while True:
    text = input('{0}, enter number: '.format(name))
    if text == "stop":
        print("You left the program! See you again! Number was guessed", n)
        break 
    elif int(text) == n:
        print("{0}!,You win!!!".format(name))
        break
    else:
        print("Try again")