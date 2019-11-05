A = [ 55, -8, 43, 52, 8, 59, -91, -79, -18, -94 ]
subA = []
addA=[]
for i in range(0,len(A)):
    subA.append(A[i]-(i+1))
    addA.append(A[i]+(i+1))
subA.sort()
addA.sort()

maxi = max(subA[-1]-subA[0],addA[-1]-addA[0])

print(maxi)