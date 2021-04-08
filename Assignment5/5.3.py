n=int(input('fibonachi serie len\n'))
f1=0
f2=1
f=[]
if n==0:
    f=f1
elif n==1:
    f=[f1,f2]
else:
    for i in range(2,n):
        f=[f1,f2]
        a=f1+f2
        f.append(a)
        f1=f2
        f2=a
print(f)

f_tuple=tuple(f)
print(f_tuple)