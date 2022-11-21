def get_digits(number):
    string = [int(i) for i in str(number)]
    tup_num = tuple(string)
    print('list of numbers:', tup_num)
get_digits(input("enter number: "))