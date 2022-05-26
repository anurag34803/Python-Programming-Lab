Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# dict store factorial of key number
# method first when key and value both are int

''' dct = {
       1 : 1,
       2 : 4 ,
       3 : 6 ,
       4 : 24 ,
       5 : 120
    }
    
print(f"Sum of values is {sum(dct.values()) }")  
print(f"Sum of keys is {sum(dct.keys()) }") '''


# note it is also possible value in string 

dct = {
       '1' : '1',
       '2' : '4' ,
       '3' : '6' ,
       '4' : '24' ,
       '5' : '120'
    }

keys_sum = [int(i) for i in dct]
value_sum = [int(dct[i]) for i in dct]

print(f"Sum of values is {sum(value_sum)}")  
print(f"Sum of keys is {sum(keys_sum)}")
