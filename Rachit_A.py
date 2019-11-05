n= int(input())
s =input()
q = int(input())
ls = []

for i in range(n):
    char_count = dict()
    for c in s[:i]:
        if c in char_count:
            char_count[c]+=1
        else:
            char_count[c] = 1
    ls.append(char_count)

for x in range(q):
    ind = int(input())
    k = s[ind-1]
    if k in ls[ind-1]:
        print(ls[ind-1][k])
    else:
        print("0")


