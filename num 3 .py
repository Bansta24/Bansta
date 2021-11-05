from functools import wraps

def type_logger():
    @wraps(func)
    def wrapper(*args):
        for i in args:
            print(f'{func.__name__}({arg}: { type (arg)})', end=(','))
        return func(*args)
    return wrapper()



