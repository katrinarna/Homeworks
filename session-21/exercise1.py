def register_call(func):
    def wrapper(arg):
        print(f"{func.__name__} was called with argument {arg}")
        return func(arg)
    return wrapper


@register_call
def foo(a):
    return 2 * a

a = foo(2)
b = foo(4)
c = foo(12)

print(a,b)

from datetime import datetime

def register_call(func):
    def wrapper(arg):
        
        timestamp = datetime.now()
        
        result = func(arg)
        
        print(f"[{timestamp}] {func.__name__} was called with argument {arg} and returned {result}")
        return result
    return wrapper

@register_call
def foo(a):
    return 2 * a

foo(2)
foo(5)
foo(10)