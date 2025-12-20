# break and continue

i = 1
while (i<=10):
    if(i%6==0):
        break
    print(i)
    i+=1 
        
print()

x = 1
while(x<=10):
    if(x%3==0):
        x+=1
        continue
    print(x)
    x+=1

# Print all odd nums 1 to 10
n = 0
while(n<10):
    n+=1
    if(n%2==0):
        continue
    print(n)