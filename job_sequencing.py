from dataclasses import dataclass

@dataclass
class Job :
    jn:int                       #job number
    pr:int                       #job profit
    dl:int                       #job deadline
    

    def __init__(self,j,p,d):
        self.jn=j                  
        self.pr=p                  
        self.dl=d                  
    
    ''' function to get job name'''
    def get_jn(self):
        return(self.jn)
    
    ''' function to grt profit'''
    def get_pr(self):
        return(self.pr)
    
    ''' function to get deadline'''
    def get_dl(self):
        return(self.dl)

class JobSeq :
    def __init__(self,):
        self.d=[]                  #list of jobs
    
    ''' function to add job to job seq list'''
    def add(self,i):
        self.d.append(i)
     
    
    ''' function to sort job seq'''    
    def sorted(self):
        #sorting acc to deadline
        self.d.sort(key=lambda item:item.get_dl(),reverse= False)
        #sorting futher acc to profit
        j=1                           #dead line for comparision
        list1=[]                      #list of  sorted jobs
        list2=[]                      #list of sorting  jobs
        for i in self.d:
            if(i.get_dl()==j):
                list2.append(i)
                
            if(i.get_dl()==j+1):
                list2.sort(key=lambda item:item.get_pr(),reverse=True)
                list1=list1+list2
                list2=[]
                list2.append(i)
                j=j+1
        list2.sort(key=lambda item:item.get_pr(),reverse=True)
        list1=list1+list2
        self.d=list1    
    
    
    ''' function to process job sequencing'''       
    def process_job_seq(self):         
        res=JobSeq()                              #result of job sequencing
        n=self.d[len(self.d)-1].get_dl()          #length of res
        j=1                                       #job deadline for comperision
        for i in self.d:
            if(i.get_dl()==j and j<=n):
                res.add(i)
                j+=1
        return res
    
    ''' function to display JobSeq object'''
    def display(self):
        print(self.d)   
        
        
js=JobSeq()
j1=Job(1,100,2)
js.add(j1)
j2=Job(2,200,1)
js.add(j2)
j3=Job(3,150,2)
js.add(j3)
j4=Job(4,250,1)
js.add(j4)
js.sorted()
js_res=js.process_job_seq()
js_res.display()
