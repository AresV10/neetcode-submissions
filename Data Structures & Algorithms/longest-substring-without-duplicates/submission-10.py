class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_substing = {}
        maxsub,start= 0,0
        for i, char in enumerate(s):
            index = curr_substing.get(char, -1)
            if index >= start:
                maxsub = max(maxsub, i-start)
                start = curr_substing[char]+1
            curr_substing[char] = i
        
        return max(maxsub, len(s)-start)
            