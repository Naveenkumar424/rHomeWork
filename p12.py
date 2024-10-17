#insertion sort
a = [1,0,6,4,3]
for i in range(1,len(a)):
    curr = a[i]
    prev = i-1
    while(prev>=0 and a[prev]>curr):
        a[prev+1] = a[prev]
        prev -= 1
    a[prev+1] = curr
print(a)
#end of code