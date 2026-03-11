#Swapping two numbers
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
# a, b = b, a
# print("After swapping: a =", a, "b =", b)
a= a+b
b= a-b
a= a-b
print("After swapping: a =", a, "b =", b)