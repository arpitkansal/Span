list1 = list(map(int,input().split(',')))
list2 = list(map(int,input().split(',')))

len1 = len(list1)
len2 = len(list2)

if len1 <len2:
    final_len = len1
    final_list = list2
    temp_list = list1

else:
    final_len = len2
    final_list = list1
    temp_list = list2

for i in range(final_len):
    final_list[i] = final_list[i] + temp_list[i]

print(final_list)