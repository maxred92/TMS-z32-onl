from datetime import datetime
from functools import wraps
def log_function(f):
    @wraps(f)
    def wrapper(*args):
        print(f"{datetime.now()} | Function: {f.__name__} | Expected: {f.__annotations__} | Input: {args}")
        return f(*args)
    return wrapper
@log_function
def test(a: int, b: str):
    return test

test(1, 'time')