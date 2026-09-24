class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while (right - left) >1:
            mid = (right + left)//2
            if nums[mid] > nums[right]:#min on right half
                left = mid
            else:# nums[mid] < nums[right]:#on left half
                right = mid
            print(mid, right)
        return min(nums[left], nums[right])