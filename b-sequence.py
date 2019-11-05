n = int(input())
nums = list(map(int,input().split()))
q = int(input())
max_num = max(nums)
nums_count_dict = dict()
total_count = len(nums)
for i in range(n):
    if nums[i] in nums_count_dict:
        nums_count_dict[nums[i]] += 1
    else:
        nums_count_dict[nums[i]] = 1

while(q):
    x = int(input())

    if x>max_num:
        nums.insert(nums.index(max_num)+1,x)
        max_num = x
        total_count += 1
        print("max")

    if x<max_num:
        exist_count = nums_count_dict.get(x,0)

        if exist_count == 0:
            print("0")
            nums_count_dict[x] = 1
            total_count += 1
            i = 0
            cur_num = nums[i]

            while x>cur_num:
                i += 1
                cur_num = nums[i]
            nums.insert(i,x)
        if exist_count == 1:
            print("1")
            i = nums.index(max_num)
            cur_num = nums[i]
            while x<cur_num and i<(len(nums)-1):
                i += 1
                cur_num = nums[i]
            if x<nums[-1]:
                nums.insert(len(nums),x)
            else:
                nums.insert(i, x)
            nums_count_dict[x] += 1
            total_count += 1
    print(nums)
    print(total_count)

    q -= 1

print(nums)