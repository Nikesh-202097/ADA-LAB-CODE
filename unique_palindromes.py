'''function to break sentence into words'''
def split (str):
    str1=[]
    i=0
    for j in range(0,len(str)):
        if(str[j]==" "):        #check starting of next word and add to list
            str1.append(str[i:j])
            i=j+1
        elif(j==len(str)-1):    #check last word and add to list
            str1.append(str[i:])
            
    return str1
        
        
''' function to check str is palindrome or not '''              
def palindromes(str):
    strf=[]
    str1=split(str)
    
    for i in str1:      #perfom operation on strings in list ,i is a string
        is_pa=True
        for j in range(0,len(i)):
            
            k=len(i)-j-1    #backtracking at same time
            if(j<k and i[j]==i[k]): # check condition of palindrome
                is_pa=True
            elif(j>k):          #check for terminate
                break
            elif(i[j]!=i[k]):   #check for terminate
                is_pa=False
                break
        if(is_pa==True):        #add string to result
            strf.append(i)
    return strf

stri="hanah asked sarah but sarah refused" 
strf=palindromes(stri)
print(strf) 
          
            