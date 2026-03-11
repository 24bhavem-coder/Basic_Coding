# Python Conditional Statements (if-else)
no = int(input("Please enter a number: "))

if no > 0:
    print("The number is positive.")
    
elif no < 0:
    print("The number is negative.")
    
else:
    print("The number is zero.")

# accept day from user and check whether it's a working day or weekend using if-else statement
day = input("Please enter a day: ")
day = day.capitalize() 
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a working day.")
else:
    print("It's a weekend.")

# accept marks of three papers and calculate total and percentage and check whether the student is eligible for placement or not using if-else statement. (Eligibility criteria: percentage should be greater than 60%)
marks1 = float(input("Enter marks for paper 1: "))
marks2 = float(input("Enter marks for paper 2: "))
marks3 = float(input("Enter marks for paper 3: "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

if percentage > 60:
    print("The student is eligible for placement.")
else:
    print("The student is not eligible for placement.")