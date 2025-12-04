
age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote")
    print("You can Drive")
else:
    print("You can't vote")

color = input("Enter a color of traffic lights : ")

if color == "red":
    print("Stop!!")
elif color == "green":
    print("Go!!")
elif color == "yellow":
    print("Look !!")
else:
    print("Wrong traffic light color entered")