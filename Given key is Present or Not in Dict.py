# Check given is present or not

key = input("Enter Key\n")                                          #Searched Key
dct = {
       'Apple' : 1,
       'Mango' : 4 ,
       'Banana' : 6 ,
       'Cheery' : 24 ,
       'Grapes' : 120
    }
    
for i in dct:
    if(key == i):
        print("Entered Key is Available")
        break
    
else:
    print("Enter Key is not Available")
