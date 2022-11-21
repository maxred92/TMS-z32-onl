a = str(input("word_1: "))
b = str(input("word_2: "))
c = str(input("word_3: "))
a, b, c = set(a), set(b), set(c)
exer_1 = a & b & c
exer_2 = a|b|c
exer_3 = (a-b-c)|(b-a-c)|(c-a-b)
print(" ".join(exer_2), " ".join(exer_1)," ".join(exer_3), sep = '\n')

