a = input()
a = a.split()

for i in a:
    if(int(i)%2==0):
        print(i, "is Even")
        
    else:
        print(i, "is Odd")
