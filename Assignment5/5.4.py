n=int(input('please enter number of rows\n'))
m=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    m[i][0]=1

for i in range(1,n):
    for j in range (1,i):
        m[i][j]=m[i-1][j]+m[i-1][j-1]
        
for i in range(n):
    for j in range(i):
        print(m[i][j],end=' ')
    print()
