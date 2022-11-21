def non_split(text):
   word = []
   t = []
   for i in text:
       if i == ' ':
           word.append(''.join(t))
           t = []
       elif i != ' ':
           t.append(i)
   if t:
       word.append(''.join(t))
   return word
a = input("enter a sentence: ")
print(non_split(a))