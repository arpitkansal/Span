left = 1
right = 22
nums = list()
for i in range(left,right+1):
    flag = 0
    for j in str(i):
        if int(j) == 0 or i%int(j) != 0:
            flag = 1
            break
    if flag==0:
        nums.append(i)

print(nums)
