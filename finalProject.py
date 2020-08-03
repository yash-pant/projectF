import random

count = 0
a = 0
b = 0
c = 0
d = 0
e = "ERROR 404 PAGE NOT FOUND... PLEASE CHECK YOUR INPUT AGAIN"
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0 
z = 0

print()
print()
print("WELCOME TO JALIGAS CHEMISTRY GAME!")
print()
print("WE HAVE LOTS OF FUN IN STORE FOR YOU TODAY!")
print()
while True:
    a = input("How many Players are playing today...(Please give a number answer of '1' or '2')  ")
    if a == "1":
        print()
        print("You have said that there is only " + str(a) + " player...")
        b = input("Is this correct?(please answer 'y' or 'n') ")
        print()
        if b == "y":
            break
        elif b == "n":
            print("Okay Lets try this again...")
        else:
            print(e)
    elif a == "2":
        print()
        print("You have said that there are only " + str(a) + " players...")
        b = input("Is this correct?(please answer 'y' or 'n') ")
        print()
        if b == "y":
            break
        elif b == "n":
            print("Okay Lets try this again...")
        else:
            print(e)        
    else:
        print(e)


