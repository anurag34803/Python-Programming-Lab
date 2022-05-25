a = input("Enter Values\n")
a = a.split(",")

for i in a:
    factorial = 1
    i = int(i)
    for j in range(2,i+1):
        factorial = factorial*j
    print("factorial of",i,"is",factorial)
