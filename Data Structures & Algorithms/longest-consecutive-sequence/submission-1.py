class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        max_count = 0
        for num in lookup:
            curr_count = 0
            if num-1 not in lookup:
                counter = num
                while counter in lookup:
                    curr_count+=1
                    counter+=1
            max_count = max(max_count, curr_count)

        return max_count