row = int(input("Enter Row\n"))
number = 1

for i in range(row):
    for j in range(i+1):
        if(number>9):
            number = 1
        print(number,end=" ")
        number +=1 
    print()
