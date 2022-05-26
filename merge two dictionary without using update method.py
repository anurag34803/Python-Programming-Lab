# merge two python dictionaries

a = {
        'first': 'Anurag',
        'sec' : 'H'
    }
    
b = {
        'Rollno' : 20
    }
    
for i in b:
    a[i] = b[i]
    
print(a)
