A = str(100010000)
ans = []
num0 = 0
num1 = 0
A = list(i for i in A)

setA = set(A)
setA = list(setA)
if len(setA)==1 and setA[0]==1:
    print(ans)
index_dict = {}
for i in range(len(A)):

    if A[i]=='0':
        num0 += 1

    elif A[i]=='1':
        num1 += 1

    lis = [num1,num0]
    index_dict[i+1] = lis
print(index_dict)

