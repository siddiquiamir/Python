# Implicit Line condition
a= [1,2,3]

a= [1,
    2,
    3]

print(a)

a= [1, # item 1
    2, # item 2
]
print(a)

a= (1  #comment
    ,2 # comment
    ,3 # comment
    )
print(a)

a= {"key1": 1 # value for key 1
    , "key2": 2 # value for key 2
    }
print(a)

def my_func(a, # this is a
            b, # this is b
            c # this is c
 ):
    print(a,b,c)

my_func(10,20,30)

# Explicit Line Condition
a= 10
b= 20
c= 30

if a > b \
    and b > c \
        and c > a :
    print("This is True")
else:
    print("This is false")


# Print multi line string
def my_func():
    a= '''This is a multi line string
Keep writing'''
    return a

print(my_func())

account_id = 1001
print(account_id)

# If condition
a= 6
if a > 10:
    print(True)
else:
    print(False)

# Nested if statement
a= 10

if a < 5:
    print("a < 5")
else:
    if a < 10:
        print("5 >= a < 10")
    else:
        print(" a >= 10")

# Elif condition
a= 10
if a < 5:
    print("Less than 5")
elif a < 6:
    print("Less than 6")
elif a < 7:
    print("Less than 7")
else:
    print("Greater than 10")

a=100
b= "a < 5" if a < 5 else "a > 5"
print(b)

# Directly print the condition
print("a < 5" if a < 5 else "a > 5")

# Function
def my_func(a,b):
    return a*b

print(my_func(2,3))

print(my_func("you",3))

print(my_func([1,2,3],3))

# Lambda function
print(lambda x : x**2)

# While Loop
i= 5
while True:
    print(i)
    if i >= 5:
        break

i= 0
while i <=5:
    print(i)
    i+=1

name = input("Please enter your name: ")
while not True:
    if type(name)== str:
        print(name)
    else:
        if type(name)== int:
            input("Please enter a valid name")
            break


# While Not
min_length = 2
name = input("Please enter your name")
while not (len(name) > min_length and name.isalpha() and name.isprintable()):
    name= input("Please enter your name")
print("Hello", name)

Same code
min_length= 2
while True:
    name= input("Please enter your name: ")
    if len(name) > min_length and name.isprintable() and name.isalpha():
        break

print("Your name is", name)

Continue statement

i=0
while i < 10:
    i+=1
    if i % 2 ==0:
        continue
    print(i)

# While with else
l=[10,20,30]
print(l)
val= 100
idx= 0

while idx < len(l):
    if l[idx]== val:
        break
    idx += 1
else:
    l.append(val)
print(l)

# Try and Except
a=10
b= 0

# Try and Except
try:
    a/b
except ZeroDivisionError:
    print("Division By Zero")

# Finally
try:
    a/b
except ZeroDivisionError:
    print("Division By Zero")
finally:
    print("Finally always run")

print("====================")
# Try continue
a=0
b= 2
while a < 4:
    print("-------------------")
    a+= 1
    b-= 1
    try:
        a/b
    except ZeroDivisionError:
        print("{0} {1} Division by 0".format(a,b))
        continue
    finally:
        print("{0} {1} Always executes".format(a, b))

    print("{0} {1} main loop".format(a,b))

# Try Break
a=0
b= 2
while a < 4:
    print("-------------------")
    a+= 1
    b-= 1
    try:
        a/b
    except ZeroDivisionError:
        print("{0} {1} Division by 0".format(a,b))
        break
    finally:
        print("{0} {1} Always executes".format(a, b))

    print("{0} {1} main loop".format(a,b))

# Try Break (Code will exhaust and stop)
a=0
b= 10
while a < 4:
    print("-------------------")
    a+= 1
    b-= 1
    try:
        a/b
    except ZeroDivisionError:
        print("{0} {1} Division by 0".format(a,b))
        break
    finally:
        print("{0} {1} Always executes".format(a, b))

    print("{0} {1} main loop".format(a,b))

# For Loop (This will print tuple)
for i in [(1,2), (3,4), (5,6)]:
    print(i)

# Unpack tuple
for i,j in [(1,2), (3,4), (5,6)]:
    print(i,j)

# Continue
for i in range(5):
    if i ==4:
        continue
    print(i)

# Break
for i in range(5):
    if i ==4:
        break
    print(i)

# Try
for i in range(5):
    print("====================")
    try:
        10/(i-3)
    except ZeroDivisionError:
        print("Divided by zero")
        continue
    print("Main body")

# Print Index
s= "hello"
for i in range(len(s)):
    print(i)

# Print Index and elements
s= "hello"
for i in range(len(s)):
    print(i, s[i])