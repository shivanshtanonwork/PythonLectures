# Match Case in Python

color = input("Enter color : ")

match color:
    case "green":
        print("Go")
    case "yellow":
        print("Look")
    case "red":
        print("Stop")
    case _:    #Default case
        print("Wrong color")