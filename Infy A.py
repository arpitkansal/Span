n = int(input())
nums = []
strLis = []
rotation_sums = []
for _ in range(n):
    s = input()
    nums.append([int(i) for i in s])
    strLis.append(s)
count_list = []
for i in range(n):
    digits_count = dict()
    for j in range(len(nums[0])):
        cur_num = nums[i][j]
        if cur_num in digits_count:
            digits_count[cur_num] +=1
        else:
            digits_count[cur_num] = 1
    count_list.append(digits_count)

flag = 1
for i in range(len(count_list)-1):
    if(count_list[0]==count_list[i+1]):
        flag =1

    else:
        flag = -1
        break
flg =0
if flag == -1:
    print("-1")
else:
    for i in range(n):
        refer = strLis[i]
        num_rot =0
        for j in range(n):
           newStr = strLis[j]+strLis[j]
           try:
            num_rot += newStr.index(refer)

           except:
            flg = -1
            break

        rotation_sums.append(num_rot)
    if flg == -1:
        print("-1")
    else:
      #  print(rotation_sums)
        print(min(rotation_sums))
