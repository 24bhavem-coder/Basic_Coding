#Height of user in feet and convert into centimeters and inches
def convert_height(feet):
    centimeters = feet * 30.48
    inches = feet * 12
    return centimeters, inches


h = float(input("Enter your height in feet: ")) 
cm, inc = convert_height(h)
print("Height in centimeters:", cm)
print("Height in inches:", inc)