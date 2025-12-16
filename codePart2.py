
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

age = int(input("enter age: "))

if (age < 13):
    print("child")
elif (age>=13 and age < 18):
     print("teenager")
else:
     print("adult")

username = input("Enter a username : ")
password = input("Enter a password : ")

if (username == "admin" and password == "pass"):
    print("Admin login!!")
elif (username != "admin"):
    print("Wrong username")
elif (password != "pass"):
    print("Wrong password")
else:
    print("Access denied.!")


n = int(input("Enter a number : "))

if(n%5 == 0):
    print("multiple of 5")
else:
    print("not multiple")