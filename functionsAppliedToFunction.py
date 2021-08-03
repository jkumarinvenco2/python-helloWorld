def mult_by_five(x):
    return x * 5

def call(fn, arg):
    """
    Call fn on arg
    :param fn:
    :param arg:
    :return:
    """
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n'
)