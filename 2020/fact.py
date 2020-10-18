#FACTORIAL OF A NUMBER IN PY
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
n = int(input("Enter the number:"))
print("fact:",fact(n))
