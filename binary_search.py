'''function for searching key in list by binary search'''
def binary_search(list,key):
    n=len(list)            
    mid=n//2        # mid is the mid index of list
    # check list is empty or not
    if(n==0):       
        return -1
    else:
        
        if(list[mid]==key):
            return mid
        elif(list[mid]>key):
            return binary_search(list[0:mid],key)
        else:
            return binary_search(list[mid+1:n],key)


list=[1,2,3,4,5,6]
key=1
pos=binary_search(list,key)

if(pos==-1):
    print("key not found") 
else:
    print("key found at ",pos)  

   