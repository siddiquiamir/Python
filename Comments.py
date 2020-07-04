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
