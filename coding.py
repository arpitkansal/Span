t = int(input())

while(t):
        str = input().split()
        i=0
        j=0
        m = len(str[0])
        n = len(str[1])
        z = 1
        x=0
        y=0
        while i < m and j<n:

            if str[1][j] == str[0][i]:
                y +=1
                if y==1:
                    x = i
                z += (i-x-1)
                x = i
                j +=1

            i += 1
        if j==n:
            print("YES",z)
        else:
            print("NO")
        t = t-1
