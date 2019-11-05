class Solution:
    def twoSum(self, nums , target):
        length = len(nums)
        num_wd_index = {}
        for i in range(length):
            num_wd_index[nums[i]] = i
        for i in num_wd_index:
            k = target - i

            j = num_wd_index.get()
            if (j != -1 and j != num_wd_index[i]):
                return (num_wd_index[i], j)
                break
s = Solution()
