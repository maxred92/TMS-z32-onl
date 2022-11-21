name = input("enter your name: ")
while True:
    age = int(input("how old are you? "))
    if age > 18:
        print(name,",today you can drink beer:)")
    elif age == 18:
        print(name,",today you can drink beer:)")
    elif age < 18:
        print(name,",you can't drink beer now!:(")
