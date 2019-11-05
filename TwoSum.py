class Solution:
    def twoSum(self, nums , target):
        length = len(nums)
        # num_wd_index = {}
        # for i in range(length):
        #     num_wd_index[nums[i]]=i
        for i in range(length):
            k = target - nums[i]
            try:
                j = nums.index(k,i+1,length)
                return(i,j)
            except:
                continue
s1 = Solution()
print(s1.twoSum([3,3],6))