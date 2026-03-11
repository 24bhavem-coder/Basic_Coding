#Reverse the number and string
num = 1234567
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)

# num = 123
# print(num)
# a = num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a * 100 + b * 10 + c
# print("Reversed number:", rev)