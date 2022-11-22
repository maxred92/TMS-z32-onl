n = (36,72,546,1,76,45,99,1973)
print(tuple(filter(lambda n : int(sum(list(int(i) for i in str(n)))) % 9 == 0, n)))
