# For loops

string = "Hello"

if 'o' in string:
    print("Yes o exists in string")

for var in string:
    print(var)

for i in range(5):
    print(i+1)

word = "artificial intelligence"
#count the number of i's 
count = 0
for ch in word:
    if(ch == "i"):
        count+=1
print("count of i = ",count)