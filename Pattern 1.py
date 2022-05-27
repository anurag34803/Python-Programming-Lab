a = int(input("Enter Lines\n"))

for i in range(1,a+1):
    for j in range(1,a):
        print(" ",end=" ")
        
    for k in range((2*i)-1):
        print("*",end=" ")
    
    for j in range(1,a):
        print(" ",end=" ")    
    
    print()
    a = a-1
