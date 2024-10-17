#Bubble sort
a = [1,0,6,5,3]
for turn in range(len(a)-1):
    for inner in range(len(a)-turn-1):
        if(a[inner+1]<a[inner]):
            a[inner],a[inner+1] = a[inner+1],a[inner]
print(a)
#end of code