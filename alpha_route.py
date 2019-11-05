alpha_coord_dict = dict()
alpha_coord_dict = {'a' : [1,1], 'b' : [1,2],'c' : [1,3],'d': [1,4], 'e': [1,5], 'f': [2,1], 'g': [2,2], 'h': [2,3],
                    'i': [2,4], 'j': [2,5], 'k': [3,1], 'l': [3,2], 'm': [3,3], 'n': [3,4], 'o': [3,5], 'p': [4,1],
                    'q': [4,2], 'r': [4,3], 's': [4,4], 't': [4,5], 'u': [5,1], 'v': [5,2], 'w': [5,3], 'x': [5,4],
                    'y': [5,5], 'z': [6,1]}
word= "zdz"
curr = [1,1]
arr = []
for i in word:
    reach = alpha_coord_dict[i]
    diff1 = curr[0]-reach[0]
    diff2 = curr[1]-reach[1]
    print(diff1, diff2)
    while diff1 < 0:
        arr.append('D')
        diff1 += 1
        #print("1")
    while diff1 > 0:
        arr.append('U')
        diff1 -= 1
        #print("2")
    while diff2 < 0:
        arr.append('R')
        diff2 += 1
        #print("3")
    while diff2 > 0:
        arr.append('L')
        diff2 -= 1
        #print("4")
    if diff1==0 and diff2==0:
        arr.append('!')
    curr[0] = reach[0]
    curr[1] = reach[1]
print(''.join(arr))