class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while (right - left) >1:
            mid = (right + left)//2
            if nums[mid] > nums[right]:#min on right half
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])