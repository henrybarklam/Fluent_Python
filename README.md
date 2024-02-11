# Fluent_Python

Class methods in Python will always take 'self' (technically you can call it whatever you want, but 'self' is the most common) as an argument to refer to the object being called - in C++ and Java this is hidden 

All of the code at the bottom is set off by an if clause, which checks to see if something called __name__ us equivalent to __main__ 

The reason for the if is that any file can also be used as a library module within another program (modules are described shortly). In that case, you just want the classes defined, but you don’t want the code at the bottom of the file to be executed. This particular if statement is only true when you are running this file directly; that is, if you say on the command line. However, if this file is imported as a module into another program, the __main__ code is not executed.

To create an object level field you just name it using 'self' inside one of the methods (usually within the constructor but not always)

In a dynamically typed language like Python, the type of a variable is determined at runtime, not necessarily at compile time. This means you can assign different types to the same variable during the execution of the program

Every time you create a file, you implicitly create a module (Java uses packages) with the same name of the module - Python searches the PYTHONPATH in the same way that JAVA searches CLASSPATH and reads the file.

You inherit a class by listing the names of the class inside parentheses after the name of the inheriting class.

You can turn a list into function arguments using *: 
x = [1,2,3]
f(*x)
f(*(1,2,3))

# Python Decorators
The only constrain upon the object returned by thedecorator is that it can be used as a function - which basically means it must be callable. Any classes we use as decorators must implement __call__.

The act of decoration replaces the object its being called on

You used to have to do something like the following: 
    def foo(): pass
    foo: staticmethod(foo)

With the addition of the @ decoration operator you now get the same result by saying:
@staticmethod
def foo(): pass

The @ decoration operator is just a little syntax sugar meaning "pass a function object through another function and assign the result to the original function"