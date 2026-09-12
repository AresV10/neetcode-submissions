class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr, l , r = 0, 0, len(heights) -1
        while l != r:
            maxAr = max(maxAr, (r-l)*min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return maxAr