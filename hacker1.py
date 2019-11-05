arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for p in range(len(arr)):
    q = 0
    while (q <= p):
        newArr = arr[q:len(arr) - p + q]
        q += 1
        print(newArr)