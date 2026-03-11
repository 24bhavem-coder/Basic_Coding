name = input("Please enter your name: ")
print("Hello, " + name + "! Welcome to the programming world!")
print('Z' in name)
print('Z' not in name)

for i in range(2, 11, 2):
    print(i)  
print("Loop is finished.")

for i in range(1, 11):
    print(i*3)

for i in range(1, 21):
    print(f"Table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

for i in range(1, 11):
    print(f"{i*2} | {i*3} | {i*4} | {i*5} | {i*6} | {i*7} | {i*8} | {i*9} | {i*10}")
