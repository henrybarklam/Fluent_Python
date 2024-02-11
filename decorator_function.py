'''
The constructor for my_decorator is executed at the point of decoration of the function

'''



class my_decorator(object):
    
    def __init__(self,f) -> None:
        print("inside my_decorator.__init__")
        f()
    def __call__(self):
        print("inside my_decorator.__call__()")


@my_decorator
def aFunction() -> None:
    print("inside aFunction")

print("Finished decorating aFunction")

aFunction()