from collections import Counter
def combine_dicts(*args):
    lists = [Counter(d) for d in args]
    result = Counter()
    for d in lists:
        result += d
    return dict(result)
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100} 
print(combine_dicts(dict_1, dict_2, dict_3))

