A = [1,3,4,2,5,6,8,3]
dictt = {}
rA = rB = 0
for i in A:
    if i in dictt:
        dictt[i] += 1
    else:
        dictt[i] = 1
for i in range(1,len(A)+1):
    key  = dictt.get(i,-1)
    if(key==2):
        rA = i
    if (key==-1):
        rB = i
    if rA and rB:
        break
print(rA, rB)
