"""
Flow control in Python
keywords: if, elif, else, and, or, not
        for, while, break, continue, pass
"""

# comparison operators
x = 2
print(x == 2)  # True
print(x == 3)  # False
print(x < 3)   # True
print(x <= 2)  # True
print(x != 3)  # True


# indentation is important.  1 Tab = 4 spaces
if 5 > 2:
    # iff true
    print("Five is greater than two!")
else:
    # iff false
    print("Five is not greater than two!")


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if not name == "John":
    print("Your name is not John.")


# elif
name = "Rick"
if name == "John":        # check first
    print("Your name is John.")
elif name == "Rick":      # check second
    print("Your name is Rick.")



# for loop
for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9

# for over iterable
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

phonebook = {"John" : 77566, "Jack" : 77264, "Jill" : 62781}
for name in phonebook.keys():
    print(name) # John Jack Jill

for number in phonebook.values():
    print(number) # 77566 77264 62781

for name, number in phonebook.items():
    print(f'Phone number of {name} is {number}')


# while loop
count = 0
while count < 5:
    print(count)
    count = count + 1


# break and continue
count = 0
while True:
    print(count) # 0 1 2 3 4
    count += 1
    if count >= 5:
        break # break out of the (nearest) loop

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue # skip the rest in the (nearest) loop
    print(x) # 1 3 5 7 9