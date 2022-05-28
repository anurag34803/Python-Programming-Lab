def pangran(x):
    x = x.upper()
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYS'
    for i in alphabets:
        if(i not in x):
            print("Not a Pangram")
            break
        
    else:
        print("Palindrome")
    
a = input("Enter String")
pangran(a)
