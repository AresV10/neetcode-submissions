class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (right + left)//2
            if nums[mid] >= nums[left]:#left half sorted 
                if target >= nums[left] and target <= nums[mid]:
                    #target in left
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    #target in right
                    left = mid+1
                else:
                    right = mid-1
            if nums[mid] == target:
                return mid
        return -1

