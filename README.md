# Fluent_Python

Class methods in Python will always take 'self' (technically you can call it whatever you want, but 'self' is the most common) as an argument to refer to the object being called - in C++ and Java this is hidden 

All of the code at the bottom is set off by an if clause, which checks to see if something called __name__ us equivalent to __main__ 

The reason for the if is that any file can also be used as a library module within another program (modules are described shortly). In that case, you just want the classes defined, but you don’t want the code at the bottom of the file to be executed. This particular if statement is only true when you are running this file directly; that is, if you say on the command line. However, if this file is imported as a module into another program, the __main__ code is not executed.

To create an object level field you just name it using 'self' inside one of the methods (usually within the constructor but not always)