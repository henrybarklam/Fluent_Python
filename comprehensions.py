import types


a_list = [1, '4', 9, 'a', 0 ,4 ]

squared_ints = [e**2 for e in a_list if isinstance(e,int)]

# Alternative

squared_ints_alt = list(map(lambda e: e**2, filter(lambda e: isinstance(e, int), a_list)))

print(squared_ints_alt == squared_ints)