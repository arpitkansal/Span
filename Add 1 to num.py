A = [9,9,9,9]

while A[0] == 0 and len(A)-1 != 0:
    A.pop(0)
i = 1
k = A[-i] + 1

while k//10 >=1:
    A[-i] = k%10
    if i==len(A):
        A.insert(0,1)
        break
    i += 1
    k = A[-i] + 1
A[-i] = k%10

print(A)
