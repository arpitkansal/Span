import gc
def primeCheck(n):
   # print(n)
    for i in range(2,int((n**0.5)+1)):
       # print(i)
        if n%i==0:
            return False
    return True
start , end = map(int,input().split())
ls=[]

for i in range(start,end+1):
    if primeCheck(i):
        ls.append(i)

print(ls)
gc.disable()
print(gc.isenabled())
ls = [123, 456]
ls2 = [1,2,3]
ls = ls2
print(gc.is_tracked([123, 456]))
print(gc.get_stats())