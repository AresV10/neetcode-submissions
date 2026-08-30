class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashres = {}
        for i, num in enumerate(nums):
            countervalue = hashres.get(num, -1)
            if countervalue >= 0:
                return [min(countervalue, i), max(countervalue, i)]
            hashres[target - num] = i

        return [0,1]