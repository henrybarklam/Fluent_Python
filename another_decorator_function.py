from typing import Any


class entry_exit(object):
    def __init__(self,f) -> None:
        self.f = f
    
    def __call__(self) -> Any:
        print(f"Entering {self.f.__name__}")
        self.f()
        print("Exiting %s" % self.f.__name__)

@entry_exit
def func1() -> None:
    print("inside func1()")

@entry_exit
def func2() -> None:
    print("inside func2")


if __name__ == "__main__":
    func1()
    func2()
