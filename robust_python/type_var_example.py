from typing import TypeVar

'''
This says that for a type T, reverse takes in a list of elements of type T
and returns a list of elements of type T - it can't mix types, a list of integers will never be able
to become a list of strings if those lists aren't using the same TypeVar
'''

T = TypeVar('T')
def reverse(coll: list[T]) -> list[T]:
    return coll[::-1]