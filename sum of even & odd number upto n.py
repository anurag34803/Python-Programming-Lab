number = int(input())
sum_odd,sum_even = 0,0

for i in range(1,number+1):
    if(i%2==0):
        sum_even+=i
        
    else:
        sum_odd+=i
        

print ('Sum of odd number is',sum_odd)
print ('Sum of even number is',sum_even)
