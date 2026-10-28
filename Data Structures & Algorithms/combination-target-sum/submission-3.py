class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        def DT_helper(pointer, path, remainingTarget):
            if remainingTarget - nums[pointer] > 0:
                temp = path[:]
                temp.append(nums[pointer])
                DT_helper(pointer, temp, remainingTarget - nums[pointer])
            elif remainingTarget - nums[pointer] < 0:
                return
            elif remainingTarget - nums[pointer] == 0:#match
                temp = path[:]
                temp.append(nums[pointer])
                result.append(temp)
                return
            if pointer < len(nums)-1:
                DT_helper(pointer+1, path, remainingTarget)
        DT_helper(0, [], target)
        return result