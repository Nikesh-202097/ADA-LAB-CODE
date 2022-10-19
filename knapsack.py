from dataclasses import dataclass

@dataclass
class Kitem:
    wt:int
    pr:int
    
    def get_wt(self):
        return (self.wt)
    
    def get_pr(self):
        return (self.pr)
    
@dataclass
class Knapsack:
    k=[]                               #global variable contain kitems
    max_pr:int =0                      #maximum profit of  all kitems
  
    ''' function to add kitem '''
    def add(self,i):
        self.k.append(i)
        
    ''' function to set maximum profit '''
    def set_max_pr(self,p):
        self.max_pr=self.max_pr+p
        
    ''' function to grt maximum profit '''
    def get_max_pr(self):
        return (self.max_pr)
    
    ''' function to process knapsack problem with passing wt limit'''
    def process_knapsack(self,w):
        res=Knapsack()
        self.k.sort(key=lambda item:item.get_pr(),reverse=True)
        for i in self.k:
            if(w<i.get_wt()):
                break
            res.add(i)
            res.set_max_pr(i.get_pr())
            w=w-i.get_wt()
        return res.get_max_pr()
    
    
    def display(self):
        print(self.k)
    
itm1=Kitem(10,60)
ksack=Knapsack()
ksack.add(itm1)
itm2=Kitem(20,130)
ksack.add(itm2)
itm3=Kitem(30,300)
ksack.add(itm3)
print(ksack.process_knapsack(50))

