row = 5

for l in range(0,2):
    if(l==0):
        for i in range(1,6):
            for m in range(row,1,-1):
                print(" ",end=" ")
                
            for n in range((2*i)-1):
                print("*",end=" ")
                
            for o in range(row,1,-1):
                print(" ",end=" ")
                
            row = row-1
            print()
            
    else:
        space = 1
        for i in range(4,0,-1):
            
            for d in range(space):
                print(" ",end=" ")
                
            for n in range((2*i)-1):
                print("*",end=" ")
                
            for m in range(space):
                print(" ",end=" ")
                
            space = space+1
            print()
