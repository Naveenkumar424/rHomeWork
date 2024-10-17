#merge sort
def mergeSort(a,si,ei):
    if(si >= ei):
        return
    mid = si + (ei-si) // 2
    mergeSort(a,si,mid)
    mergeSort(a,mid+1,ei)
    merge(a,si,mid,ei)
#end of mergeSort
#Merge
def merge(a,si,mid,ei):
    i = si
    j = mid+1
    k = 0
    temp = [0]*((ei-si)+1)
    while(i <= mid and j <= ei):
        if(a[i]<a[j]):
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    while(i<=mid):
        temp[k]=a[i]
        k += 1;i += 1
    while(j<=ei):
        temp[k]=a[j]
        k += 1;j += 1
    for i in range(len(temp)):
        a[si+i] = temp[i]
    return a
#end of merge
#main section
a = [1,0,6,4,3]
mergeSort(a,0,len(a)-1)
print(a)
#end of code