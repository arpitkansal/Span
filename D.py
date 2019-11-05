n = int(input())
ls = list(map(int,input().split()))
ls.sort()
coun = dict()
for i in range(n):
    if ls[i] in coun:
        coun[ls[i]] +=1
    else:
        coun[ls[i]] = 1

maximum = max(coun, key=coun.get)  # Just use 'min' instead of 'max' for minimum.
print(coun[maximum])