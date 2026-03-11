# accept five different values in five different variables and print maximum value using simple if statements
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))

if a > b and a > c and a > d and a > e:
    print("The maximum value is:", a)
elif b > c and b > d and b > e:
    print("The maximum value is:", b)
elif c > d and c > e:
    print("The maximum value is:", c)
elif d > e:
    print("The maximum value is:", d)
else:
    print("The maximum value is:", e)