def is_safe(board,i,j):
    for k in range(j-1,-1,-1):
        if(board[i][k]==1):
            return False
    for k in range(i-1,-1,-1):
        if(board[k][j]==1):
            return False
    l=i
    m=j
    while(i>=0 or j>=0):
        if(board[i][j]==1):
            return False
    i=l
    j=m
    while(i<=n or j>=0):
        if(board[i][j]==1):
            return False    
    return True

def solve_nqueen(board,ans,n,j):
    if(j==n):
        ans.append(board)
        return
    for i in range(n):
        if is_safe(board,i,j):
            board[i][j]=1
            #print(board)
            solve_nqueen(board,ans,n,j+1)
            board[i][j]=0
            

ans=[]
print("enter board size ")
n=int(input())
board=[[0 for i in range(n)] for j in range(n)]
solve_nqueen(board,ans,n,0)
print("solutions are ")
print(ans)