a = int(input("Enter Lines\n"))

for i in  range(a):
        for j in range(a-(i+1)):
            print(" ",end="")
    
        for k in range(i+1):
            print("*",end="")
            
        for j in range((a+1)-i):
            print(" ",end="")
    
        for k in range(i+1):
            print("*",end="")
        
        print()
