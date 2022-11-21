def change(s, s_old, s_new):
    a = " "
    i = 0
    while i<len(s):
        if s[i]==s_old:
            a = a + s_new
        else:
            a = a + s[i]
        i = i+1
    return a
s = input('enter string: ')
a = change(s, '"', "'")
print(a)
print(a.replace("'",'"'))