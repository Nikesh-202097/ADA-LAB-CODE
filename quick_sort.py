''' program to implement quick sort'''

# function to swap two elements of a list at given index
def swap(list,i,j):
    temp=list[i]
    list[i]=list[j]
    list[j]=temp

# function for putting pivot element on their apropriate position    
def partition(list,s,e):
    pivot=list[e]          # considering last element as pivot element
    i=s-1                  #variable for pointing elements less than pivot
    #traversing from start inex to end index -1
    for j in range(s,e):   
        if(list[j]<pivot):  #check current element is less than pivot or not
            i+=1            
            swap(list,i,j)  #if yes than that element and next element are
                            # pointing by i,j indexies 
    
    swap(list,i+1,e)        # after that  interchange that element with pivot
    return i+1              # return index of pivot element

# function for sorting each element by recurrsive partition
def quick_sort(list,s,e):         # s, e are start and end index
    if(s<e):                      # condition for terminating recurrsion
        p=partition(list,s,e)
    
        quick_sort(list,s,p-1)    # call quick_sort for left part to pivot 
        quick_sort(list,p+1,e)    # call quick_sort for right part to pivot
       

    
    

list=[9,8,7,6,5,4,3,2,1]
print("unsorted list  ",list)
quick_sort(list,0,8)
print("sorted list  ",list)    