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

# Setting the Data Type

a = 'Hello World'
print("'Hello World' is of type ", type(a))

b = 60
print("60 is of type ", type(b))

c = 20.5
print(type(c))

d = 1j
print(type(d))

e = ["apple", "banana", "cherry"]	
print(type(e))

f = ("apple", "banana", "cherry")
print(type(f))

g = range(6)
print(type(g))

h = {"name" : "John", "age" : 36}
print(type(h))

i = {"apple", "banana", "cherry"}
print(type(i))

j = frozenset({"apple", "banana", "cherry"})
print(type(j))

k = True
print(type(k))

l = b"Hello"
print(type(l))

m = bytearray(5)
print(type(m))

n = memoryview(bytes(5))
print(type(n))

# Setting the Specific Data Type
# Try checking the type yourself

o = str("Hello World")	#string

p = int(20)	    #integer	

q = float(20.5)	    #float	

r = complex(1j)	    #complex	

s = list(("apple", "banana", "cherry")) 	#list	

t = tuple(("apple", "banana", "cherry"))	#tuple	

u = range(6)	#range	

v = dict(name="John", age=36)	#dict	

w = set(("apple", "banana", "cherry"))	#set	

x = frozenset(("apple", "banana", "cherry"))	#frozenset	

y = bool(5)	    #bool	

z = bytes(5)	#bytes	

ab = bytearray(5)	#bytearray	

bv = memoryview(bytes(5))	#memoryview