class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (right + left)//2
            if nums[mid] >= nums[left]:#left half sorted 
                if target >= nums[left] and target <= nums[mid]:
                    #target in left
                    right = mid
                else:
                    left = mid+1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    #target in right
                    left = mid
                else:
                    right = mid

        if nums[right] == target:
            return right
        else:
            return -1

