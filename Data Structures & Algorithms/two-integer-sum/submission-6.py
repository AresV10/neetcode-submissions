class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashres = {}
        for i, num in enumerate(nums):
            if num in hashres:
                countervalue = hashres[num]
                return [countervalue, i]
            hashres[target - num] = i

        raise ValueError("no solution found")