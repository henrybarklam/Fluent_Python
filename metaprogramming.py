# Classes are just objects and can be modified in the same way


class Foo:
    pass

Foo.field = 42
x  = Foo()

print(x.field)

# Next one

def howdy(self, you):
    print('Howdy' + you)

MyList = type('MyList', (list,), dict(x=42, howdy=howdy))

ml = MyList()

ml.append("Camembert")
print(ml)
print(ml.x)
ml.howdy("John")


# Note that printing the class of the class produces the metaclass
print(ml.__class__.__class__)
