# Data Types in Python

'''
Text Type:	str e.g("Hello Luv")
Numeric Types:	int, float, complex e.g(12,20.5,200000000005885241.45223) respectively
Sequence Types:	list, tuple, range e.g(list=[], tuple=(), range() )
Mapping Type:	dict e.g(dict = {})
Set Types:	set, frozenset e.g(set = (), frozenset = ?)
Boolean Type:	bool e.g (True, False)
Binary Types:	bytes, bytearray, memoryview e.g(.........)
'''
a = "Hello World"
print(type(a))

b = 60
print(type(b))

c = 20.5

d = 1j

e = ["apple", "banana", "cherry"]	

f = ("apple", "banana", "cherry")

g = range(6)

h = {"name" : "John", "age" : 36}

i = {"apple", "banana", "cherry"}

j = frozenset({"apple", "banana", "cherry"})

k = True

l = b"Hello"

m = bytearray(5)

n = memoryview(bytes(5))
