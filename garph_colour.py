def update_trial_ans(curr_color,giv_color):
    
    for i in giv_color:
        if(i==True and i not in curr_color):
            curr_color.append(i)
            

def update_curr_color(g_matrix,final_ans,trial_ans,row,giv_color,curr_color,n):
    for i in range(n):
        if(g_matrix[row][i]==1):
            if(trial_ans[i]!=None):
                for j in curr_color:
                    if(j==trial_ans[i]):
                        curr_color.remove(i)
        
        if(len(curr_color)==0):
            for i in giv_color:
                if(i==False):
                    curr_color.append(i)
                    i==True
                    break

def garph_coloring(g_matrix,final_ans,trial_ans,row,giv_color,curr_color,n):
    if(row==n):
        final_ans.append(trial_ans)
        return
    update_trial_ans(curr_color,giv_color)
    update_curr_color(g_matrix,final_ans,trial_ans,row,giv_color,curr_color,n)
    trial_ans[row]=curr_color[0]
    garph_coloring(g_matrix,final_ans,trial_ans,row+1,giv_color,curr_color,n)


def display_final_ans(final_ans):
    print("coloring solutions ")
    print(final_ans)
    

def min_color_used(giv_color):
    j=0
    for i in giv_color:
        if(i==True):
            j=j+1
    print("minimum color used is =",j)  
    
             
                
g_matrix=[[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
final_ans=[]
trail_ans=[None,None,None,None]
giv_color={'R':False,'G':False,'B':False}
curr_color=[] 
garph_coloring(g_matrix,final_ans,trail_ans,0,giv_color,curr_color,4)
display_final_ans(final_ans)
min_color_used(giv_color)       