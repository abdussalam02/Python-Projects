'''Hello there learner,
    I am sure you will find this reading usefull,
    Have a good learning Journey.'''

# This is a module which makes our output pretty
from pprint import pprint

print("1. What is Python         2. Where is Python used")
print("3. What can Python do     4. Why Python")
print("5. Good to know           6. Python Syntax compared")
print("7. For lot size           8. For advance decline")

# Taking an Input
num = int(input("Choose any number from above: "))


if num == 1:
    pprint('''Python is a high-level, general-purpose and a very popular programming language. 
    Python programming language (latest Python 3) is being used in web development, Machine Learning applications, along with all cutting edge technology in Software Industry.
    Python Programming Language is very well suited for Beginners, also for experienced programmers with other programming languages like C++ and Java.
''')

elif num == 2:
    pprint("web development (server-side), Software Development, Artificial Intelligence(AI), Machine Learning, Scientific Calculation, System Scripting.")

elif num == 3:
    pprint('''Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.''')

elif num == 4:
    pprint('''Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.''')

elif num == 5:
    pprint('''The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.''')

elif num == 6:
    pprint('''Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.''')

elif num == 7:
    pprint("Soon")

elif num == 8:
    pprint("Soon")

else:
    print("Entered Number is not valid!")