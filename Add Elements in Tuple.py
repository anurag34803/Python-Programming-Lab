tup = (5,4,3,2,1,11,10,9,8)                      #Creation of tuple
print(f"Tuple is {tup}")

remove = int(input("Enter Value For Add\n"))
tup = list(tup)                                 # convert tuple into list because tuple is immutable
tup.append(remove)

tup = tuple(tup)
print(tup)
