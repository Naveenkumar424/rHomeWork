#Quick sort
def quickSort(a,si,ei):
    if(si>=ei):
        return
    piv = partition(a,si,ei)
    quickSort(a,si,piv-1)
    quickSort(a,piv+1,ei)
#end of quick sort
#partition
def partition(a,si,ei):
    pivot = a[ei]
    i = si-1
    for j in range(si,ei):
        if(a[j]<=pivot):
            i += 1
            a[i],a[j] =a[j],a[i]
    i += 1
    a[ei],a[i] = a[i],pivot
    return i
#end of partition
#main section
a = [1,0,6,4,3]
quickSort(a,0,len(a)-1)
print(a)
#end of code