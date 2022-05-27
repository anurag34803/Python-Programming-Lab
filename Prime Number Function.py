def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return "Not a Prime Number"
            
    return "Prime Number"
    
number = int(input("Enter Number\n"))
out = prime(number)
print (number,out)
