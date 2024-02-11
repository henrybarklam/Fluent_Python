

# Note how because this is a function, 
def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    #Remember that this is returned as is, not called (ie new_f())
    return new_f

@entry_exit
def func1():
    print("inside func1")

@entry_exit
def func2():
    print("inside func2")

func1()
func2()


