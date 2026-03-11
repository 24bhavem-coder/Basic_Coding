# Python Data Collection (List)
mylist = ["prashant", "sachin", "satyarth", "pratik", 77, 66.05, True, False]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[-1])
print(mylist[2:5])
print(mylist[2:])
print(mylist[:5])
print(mylist[:])
print(mylist[1:8:2])
print(mylist[::-1])
mylist.append("harsh")
mylist.append("satyarth")
mylist.insert(2, "pratik")
mylist.insert(1, "sanket")
print(mylist)
mylist.remove("pratik")
print(mylist)
newlist = mylist.copy()
print(newlist)
print(mylist)
print("Id of mylist:", id(mylist))
print("Id of newlist:", id(newlist))
mylist = [['prashant', 'sachin', 'satyarth', 'pratik'], [77, 66.05, True, False], ['python', 'java', 'c++']]
print("example of nested list:", mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[1][1])
print(mylist[2][0])
print(mylist[2][1])
print(mylist[2][2])
list1 = ["prashant", "sachin", "satyarth", "pratik"]
print(list1*2)
list2 = [5435, 6546, 6546, 6546, 6546]
print(list1 + list2)
del list1[2]
del list2
print(list1)
list2 = [5435, 6546, 6546, 6546, 6546]
list2.clear()
print(list2)
nyname = "prashant"
mylist = list(nyname)
print(mylist)
mylist = [875689, 783564, 982349, 23623, 87364587, 655446, 23]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
math = 10
phy = 10
print(id(phy))
print(id(math))
mylist = [875689, 783564, 982349, 23623, 87364587, 655446, 23]
newlist = mylist
print("Id of mylist:", id(mylist))
print("Id of newlist:", id(newlist))