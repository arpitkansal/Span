st = ["flower","flow","flight"]

st.sort()
count = 0

if st[0][0] != st[-1][0]:
    print("")
else:
    for i in range(len(st[0])):
        if st[0][i] == st[-1][i]:
            count += 1
        else:
            break
    print(st[0][0:count])