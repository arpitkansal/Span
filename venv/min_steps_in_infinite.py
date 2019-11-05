A= [4,-4]
B = [4,5]
steps = 0
for i in range(len(A)-1):
    disA = abs(A[i+1] - A[i])
    disB = abs(B[i+1]-B[i])
    steps += min(disA,disB)
    if disA<disB:
        steps += disB-disA
    else:
        steps += disA- disB
print(steps)