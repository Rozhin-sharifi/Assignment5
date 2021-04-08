n=int (input('please enter set A number of members\n'))
m=int (input('please enter set B number of members\n'))

list_A=[]
for i in range(n):
    a=int(input('please enter set A members\n'))
    list_A.append(a)
print('list_A:',list_A)
set_A=set(list_A)

list_B=[]
for i in range(m):
    b=int(input('please enter set B members\n'))
    list_B.append(b)
set_B=set(list_B)
print('list_B:',list_B)

union=set_A.union(set_B)
intersection=set_A.union(set_A)

print('A Union B:', union)
print('A Intersection B:',intersection)