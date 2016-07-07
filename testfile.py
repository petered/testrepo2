

def my_function_that_adds_things(a, b, c=None):

    sm = a+b
    if c is not None:
        sm += c
    return sm

