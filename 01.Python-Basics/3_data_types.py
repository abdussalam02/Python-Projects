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
print(type(b))

d = 1j
print(type(b))

e = ["apple", "banana", "cherry"]	
print(type(b))

f = ("apple", "banana", "cherry")
print(type(b))

g = range(6)
print(type(b))

h = {"name" : "John", "age" : 36}
print(type(b))

i = {"apple", "banana", "cherry"}
print(type(b))

j = frozenset({"apple", "banana", "cherry"})
print(type(b))

k = True
print(type(b))

l = b"Hello"
print(type(b))

m = bytearray(5)
print(type(b))

n = memoryview(bytes(5))
print(type(b))