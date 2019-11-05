A=[[1,2][3,4][5,6]]
A_final = list()
t = 0
b = len(A) - 1
l = 0
r = len(A[0]) - 1
dir = 0
while (t <= b and l <= r):
    if dir == 0:
        for i in range(l, r + 1):
            A_final.append(A[t][i])
        t += 1
        # dir = 1

    elif dir == 1:
        for i in range(t, b + 1):
            A_final.append(A[i][r])
        r -= 1
        # dir =2
    elif dir == 2:
        for i in range(r, l - 1, -1):
            A_final.append(A[b][i])
        b -= 1
        # dir =3
    elif dir == 3:
        for i in range(b, t - 1, -1):
            A_final.append(A[i][l])
        l += 1
    dir = (dir + 1) % 4
print(A_final)