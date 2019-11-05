n = int(input())
ls = list(map(int,input().split()))
ls.sort()
flg = [0]*n
print(flg)
j = 0
x =len(ls)
for i in range(x-1):
    for j in range(1,(x)):
        print("x : ",x)
        if ls[i]<ls[j]:
            if flg[j] == 0:
                print((i, j))
                ls.remove(ls[i])
                print(ls)
                flg[j]=1
                print(flg)
                x = len(ls)
print(ls)
