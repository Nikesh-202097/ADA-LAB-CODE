''' program for merge sort '''

#function for merginging to sublists
def merge_algo(list,s,m,e):
    nl=m-s+1                 #length of left sublist
    nr=e-m                   #length of right sublist
    list_l=[None]*nl         #left sublist of nl size is created
    list_r=[None]*nr         #right sublist of nr size is created
    
    # inserting elements of left part of list to left sublist
    for i in range(0,nl):   
        list_l[i]=list[s+i]
    
    # inserting elements of right part of list to the right sublist
    for i in range(0,nr):
        list_r[i]=list[m+1+i]
        
    i=0                      #variable for traversing in left sublist
    j=0                      #variable for traversing in right sublist
    k=s                      #variable for traversing in main list
    
    #compare the each elements of sublists and add samller one to main list
    #upto the one sublist is completed
    while(i<nl and j<nr):
        if(list_l[i]>=list_r[j]):
            list[k]=list_r[j]
            j=j+1
        else:
            list[k]=list_l[i]
            i=i+1
        k=k+1

    #add remain elemnts of left sublist to main list 
    while(i<nl):
        list[k]=list_l[i]
        i=i+1
        k=k+1
    
    #add remain elements of right sublist to main list
    while(j<nr):
        list[k]=list_r[j]
        j=j+1
        k=k+1
        
            
#function for dividing list into a single element lists
#and calling for merging  
    
def merge_sort(list,s,e):
    if(s<e):                   #check single element lists generated or not
       m=(s+(e-1))//2          #find the mid index of the list
       merge_sort(list,s,m)    #calling for dividing left divided part 
       merge_sort(list,m+1,e)  #calling for dividing right divided part
       merge_algo(list,s,m,e)  #calling for merging of divided parts
    
    
list=[9,8,7,6,5,4,3,2,1]

merge_sort(list,0,8)
print(list)
