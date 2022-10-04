"""
Block comment uses triple quotes

# legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names
2myvar = "John"    # starts with a number
my-var = "John"    # contains a dash
my var = "John"    # contains a space

"""
# one line comment uses hash tag

# single quote and double quote are the same
print('Hello World')
print("Hello World")

# variable type
myint = 7                # integer
myfloat = 7.0            # float
mystring = 'hello'       # string
mybool = True            # boolean (True or False). True = 1, False = 0 in math
mylist = [1, 2, 3]       # list/array (mutable)
mytuple = (1, 2, 3)      # tuple (immutable)
myset = {1, 2, 3}        # set (unique)
mydict = {'a': 1, 'b': 2, 'c': 3}  # dictionary (key:value pairs)
mycomplex = 1 + 2j       # complex number

print(myint,
    myfloat,
    mystring,
    mybool,
    mylist,
    mytuple,
    myset,
    mydict,
    mycomplex
)

# print out the type
print(type(1))    # <class 'int'>
print(type('1'))  # <class 'str'>



# real number
a = 3
b = 2
print(a + b)   # 5 (addition)
print(a - b)   # 1 (subtraction)
print(a * b)   # 6 (multiplication)
print(a / b)   # 1.5 (division)
print(a // b)  # 1 (floor division)
print(a % b)   # 1 (modulus)
print(a ** b)  # 9 (exponentiation)
# order: expo > mult/div/mod > add/sub


# complex number
a = 1 + 2j
b = 2 + 3j
print(a + b)  # (3+5j)
print(a - b)  # (-1-1j)
print(a * b)  # (-4+7j)
print(a / b)  # (0.6153846153846154+0.07692307692307693j)
print(abs(a))  # 2.23606797749979 absolute value



# String
mystring = "Hello World"
print(mystring)           # Hello World
print(mystring[0])        # H
print(mystring[-1])       # d
print(mystring[2:5])      # llo
print(mystring[2:])       # llo World
print(mystring * 2)       # Hello WorldHello World
print(mystring + "TEST")  # Hello WorldTEST

# format string
name = "John"
age = 23
print(f"Hello, {name}. You are {age:.2f}.")  # Hello, John. You are 23.00


# String methods
mystring = "Hello World"
print(mystring.upper())    # HELLO WORLD
print(mystring.lower())    # hello world
print(mystring.split())    # ['Hello', 'World']
print(mystring.split('o')) # ['Hell', ' W', 'rld']
print(len(mystring))       # 11

# escape character \
print("Did someone say \"Hello World\"?")  # Did someone say "Hello World"?


# List
mylist = [1, 2, 3]
print(mylist)             # [1, 2, 3]
print(mylist[0])          # 1
print(mylist[-1])         # 3
print(mylist[1:])         # [2, 3]
print(mylist + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print(mylist * 2)         # [1, 2, 3, 1, 2, 3]
mylist[0] = 'one'
print(mylist)             # ['one', 2, 3]

# List methods
mylist = [1, 2, 3]
mylist.append(4)
print(mylist)             # [1, 2, 3, 4]
mylist.pop()
print(mylist)             # [1, 2, 3]
mylist.pop(0)
print(mylist)             # [2, 3]
mylist.reverse()
print(mylist)             # [3, 2]
mylist.sort()
print(mylist)             # [2, 3]

# List comprehension
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist2 = [n*2 for n in mylist]
print(mylist2)             # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# copy list
mylist1 = [1, 2, 3]
mylist2 = mylist1     # just the reference (shallow copy)
mylist2[0] = 'one'
print(mylist1)        # ['one', 2, 3]
print(mylist2)        # ['one', 2, 3]

# copy list
mylist1 = [1, 2, 3]
mylist2 = mylist1.copy()   # deep copy
mylist2[0] = 'one'
print(mylist1)             # [1, 2, 3]
print(mylist2)             # ['one', 2, 3]



# dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print(mydict)             # {'a': 1, 'b': 2, 'c': 3}
print(mydict['a'])        # 1
mydict['a'] = 10          # change value
print(mydict)             # {'a': 10, 'b': 2, 'c': 3}
print(mydict.keys())      # dict_keys(['a', 'b', 'c'])
print(mydict.values())    # dict_values([10, 2, 3])
print(mydict.items())     # dict_items([('a', 10), ('b', 2), ('c', 3)])

del mydict['a']           # delete key 'a'
print(mydict)             # {'b': 2, 'c': 3}
mydict['d'] = 4           # add key 'd'
print(mydict)             # {'b': 2, 'c': 3, 'd': 4}



# casting
x = float(3)              # 3.0
y = int(3.9)              # 3
a = str(3)                # '3'
b = int('2')              # 2
c = float('1.23')         # 1.23
d = bool(1)               # True
e = bool(0)               # False
f = list((1, 2, 3))       # [1, 2, 3]
g = tuple([1, 2, 3])      # (1, 2, 3)
h = set([1, 2, 3])        # {1, 2, 3}
i = dict(a=1, b=2, c=3)   # {'a': 1, 'b': 2, 'c': 3}



# multiple assignment
o1 = o2 = o3 = "Orange"
print(o1)
print(o2)
print(o3)
o2 = 'Apple' # independent
print(o1)    # Orange
print(o2)    # Apple


# unpacking
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)
