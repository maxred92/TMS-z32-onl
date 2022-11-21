def dictonary():
    r = {}
    while True:
        print('enter key (enter stop - exit)')
        k = input()
        if k == 'stop':
            break
        print('enter value')
        v = input()
        r[k] = v
    return r 
d = dictonary()
print(d, {v: k for k, v in d.items()}, sep = '\n')