# Slicing #

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
#  The first character has index 0.
b = "Hello, World!"
print(b[2:5])

# From the Start
b = "Hello, World!"
print(b[:5])

# To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Starts from the End
b = "Hello, World!"
print(b[-5:-2])