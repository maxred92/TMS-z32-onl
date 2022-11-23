"""написал скрипт по твоему примеру, так как не догадался до решения, а так для практики полезно:)"""



def result(f: callable):
    pre_result = None
    def wrapper(*args, **kwargs):
        nonlocal pre_result
        print(f'Last result = {pre_result}')
        curr_result = f(*args, **kwargs)
        print(f'Current result = {curr_result}')
        pre_result = curr_result
        return curr_result
    return wrapper

@result
def f(a,b):
    return a+b

f(1,40)
f(5,7)
f(3,7)
