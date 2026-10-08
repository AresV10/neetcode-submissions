class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tail = 0
        slow = nums[0]
        fast = nums[nums[0]]
        #Floyd, cycle detection, start determination
        while fast != slow :
            slow = nums[slow]
            fast = nums[nums[fast]]
        #phase 1 complete : slow setup in loop
        while nums[tail] != nums[slow]:
            slow = nums[slow]
            tail = nums[tail]
        return nums[tail]