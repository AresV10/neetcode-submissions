class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (right + left)//2
            if nums[mid] > nums[right]:#min on right half 
                left = mid+1
            else:
                right = mid
#at this point we know the pivot is at left split into two and run binary on the required side
        if target > nums[-1]:
            right = left
            left = 0
        else:
            right = len(nums)-1

        while left<right:
            mid = (right + left)//2
            if nums[mid] >= target:#target on left half 
                right = mid
            else:
                left = mid+1
        if nums[right] == target:
            return right
        else:
            return -1

