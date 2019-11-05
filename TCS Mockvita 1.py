

n, m = map(int, input().split())

queries = []

l = n * [0]
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

for i in range(len(queries)):
    for j in range(queries[i][0]-1, (queries[i][1])):
        print(j)
        l[j] += queries[i][2]

mx = max(l)
print(mx)