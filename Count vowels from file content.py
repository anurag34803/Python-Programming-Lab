f = open('sample.txt','r')
out = f.read()
out = out.upper()
count = 0
vowels = 'AEIOU'
for i in out:
    if(i in vowels):
        count+=1
        
print("Number of vowels is",count)
f.close()
