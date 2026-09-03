class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # total = 1
        # for num in nums:
        #     total *= num
        # return [total//num for num in nums]

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        length = len(nums)
        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[length-1-i] = suffix[length-i] * nums[length-i]
        
        res = []
        for x, y in zip(prefix, suffix):
            res.append(x*y)

        return res
        # [1,1,2,8]
        # [48,24,6,1]
