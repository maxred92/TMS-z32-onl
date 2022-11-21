def double_fac(n):
    if n == 1:
        return n
    else:
        return double_fac(n-2) * n
num = int(input('enter number: '))
if num < 0:
    print("You can't calculate the factorial of a negative number")
elif num == 0:
    print('Factorial of 0 is 1')
else:
    print(f'Double factotial number {num} =', double_fac(num))