#Simple Interest Calculator
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = 10000
r = 10
t = 1
print(simple_interest(p, r, t))