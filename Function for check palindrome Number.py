def palindrome(number):
    reverse = number[::-1]
    if(number == reverse):
        return "Number is palindrome"
        
    return "Not a Palindrome"

a = input("Enter Number\n")
out = palindrome(a)
print(out)
