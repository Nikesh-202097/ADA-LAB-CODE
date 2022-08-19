from math import floor


def binary_search(list,key):
    n=len(list)
    mid=n//2
    print(mid,list[mid])
    if(list[mid]==key):
        return mid
    elif(list[mid]>key):
        binary_search(list[0:mid-1],key)
    else:
        binary_search(list[mid+1:n],key)
pos=-1
list=[1,2,3,4,5,6]
key=1
pos=binary_search(list,key)
if(pos==-1):
    print("key not found") 
else:
    print("key found at ",pos)     