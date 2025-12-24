# vowel count a,e,i,o,u
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == "o" or ch == 'u'):
        count+=1
print('total vowel count = ',count)