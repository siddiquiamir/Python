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