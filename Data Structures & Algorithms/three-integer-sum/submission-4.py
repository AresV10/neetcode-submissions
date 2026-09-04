class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i, num in enumerate(nums):
            #fixed num 2 sum on rest:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two_sum_hash = set()
            for j in range(len(nums)):
                complement = -1 * (num + nums[j])
                if i==j:
                    continue
                if (complement) in two_sum_hash:
                    result.add(tuple(sorted([num,nums[j], complement])))
                else:
                    two_sum_hash.add(nums[j])
        #print(result)


        return [list(arr) for arr in result]