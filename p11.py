#selection sort
a = [1,0,6,5,3]
for turn in range(len(a)):
    minPos = turn
    for inner in range(turn,len(a)):
        if(a[inner]<a[minPos]):
            minPos = inner
    a[turn],a[minPos] = a[minPos],a[turn]
print(a)
#end of code