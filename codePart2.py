# Nesting
username = input("Enter a name ")
password = input("Enter a password ")

if (username == "Shivansh" and password == "Tandon"):
    print("Logged Inn!!")
else:
    if(username != "Shivansh"):
        print("Wrong username")
    else:
        print("Wrong password")