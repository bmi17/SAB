x = 0
def fib(n):
    global x 
    if n==1:
        x+=3
        return n
    x+=1
    if n==0:
        return n
    return fib(n-1)+fib(n-2)
lr=[]
for i in range(5):
    lr.append(fib(i))
print(lr,"\n",x)

ans0=0
ans1=1
li=[]
for i in range(5):
    li.append(ans0)
    anstemp=ans0+ans1
    ans0=ans1
    ans1=anstemp
print(li,"\n",i+1)