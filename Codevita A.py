bs = list(map(int,input().split()))
ts = list(map(int,input().split()))
at = int(input())
ses = list(map(int,input().split()))
mz = []
cv = []
for a in range(len(bs)-1):
    x = bs[a+1] - bs[a]
    tx = (x * ts[a])/100
    cv.append(tx)
for m in range(len(ses)):
    nc = 0
    if ses[m]==0:
        nc -= at

    for e in range(len(cv)):
        if ses[m]>=cv[e]:
            ses[m] = ses[m]-cv[e]
            nc+= (cv[e]/ts[e])*100
     #       print("if2",ses[m], " ", income_sum, " ", e)

   # print("else", ses[m], " ", income_sum," ", e)
    nc += (ses[m]/ts[e+1])*100
    nc  += bs[0] +at

    mz.append(nc)
    #print("exit",ses[m], " ", income_sum)
o = 0
for a in mz:
    o +=a
print(int(o))