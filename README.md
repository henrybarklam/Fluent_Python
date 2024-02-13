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
Everything in Python is an object, including functions. A class is also an object.

The only constrain upon the object returned by the decorator is that it can be used as a function - which basically means it must be callable. Any classes we use as decorators must implement __call__.

The act of decoration replaces the object its being called on

You used to have to do something like the following: 
    def foo(): pass
    foo: staticmethod(foo)

With the addition of the @ decoration operator you now get the same result by saying:
@staticmethod
def foo(): pass

The @ decoration operator is just a little syntax sugar meaning "pass a function object through another function and assign the result to the original function"

The only restriction to the result of a decorator is that it must be callable, so that it can properly replace the decorated function. In decorator_function and another_decorator_function, we've replaced the original function with an object of a class that has a __call__() method (thus callable, but really its the new object thats being called)

# Metaprogramming

To modify a class you perform operations on it like any other object - you can add and
subtract fields and methods.

Any changes you make to the class will affect all objects of that class, even
those that have already been instantiated

Metaclasses create these special 'class' objects

The default metaclass is called 'type'. When we write a class, the default 'metatype' is invoked to create that class.

Some of the functionality that was previously only available with metaclasses is now available in a simpler form using class decorators

Metaclasses create classes. Classes create instances.

'type' called with one argument produces the type information of an existing class
'type' called with three arguments creates a new class object

The arguments when invoking 'type' are the name of the class, a list of base classes and a dictionary giving the *namespace* for the class (all the fields and methods)

So the equivalent of:

    class C:
        pass

is 

    type('C', (), {})

Classes are often referred to as types - you're calling a function that creates a new type based on its arguments

# Class initialization

Remember you don't include params in the class parentheses, rather in the __init__ function

class Pizza(object):
    def __init__(self, toppings):
        self.toppings = toppings

# Using __init__ vs __new__ in Metaclasses:
__new__ is called for the creation of a new class, while __init__ is called after the class is created, to perform additional initialization before the class is handed to the caller.

The primary difference is that when overriding __new__() you can change things like the 'name', 'bases' and 'namespace' arguments before you call the super constructor and it will have an effect, but doing the same thing in the __init__ call won't get any results from the constructor call.

# Classmethods and Metamethods
A metamethod can be called from either the metaclass or from the class, but *not* from an instance
A classmethod can be called from either a class or its instances, but is not part of the metaclass

# Static Methods and Class Methods
Static methods: Methods within a class that have no access to anything else int the class (no self keyword or cls keyword). They cannot change or look at any object attributes or call other methods within the class. Use decorator @staticmethod to produce.

Class methods: Methods within a class that only have access to class variables and other class methods. They can access anything within the class, but cannot access instance attributes. TODO: Double check what is meant by this.

# Comprehensions
A list comprehension could be broken down into two component parts - a filter and a map (and a couple of lambda functions)

