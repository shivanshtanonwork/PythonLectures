# WAF to print factorial of 'n

def cal_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

n = int(input("Enter n : "))
print(cal_factorial(5))