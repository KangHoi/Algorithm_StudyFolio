a = set([1,3,3,2,5,4,7])
print(type(a)) #set

for i in a:
    print(i,end=" ") # 1 2 3 4 5 7

b = [1,2,3] 
print(type(b)) #tuple

print(b is list(b))

