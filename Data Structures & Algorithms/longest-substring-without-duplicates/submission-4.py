class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_substing = {}
        i,maxsub, start= 0,0,0
        while i < len(s):
            char = s[i]
            index = curr_substing.get(char, -1)
            if index >= 0 and index >= start:
                maxsub = max(maxsub, i-start)
                start = curr_substing[char]+1
            curr_substing[char] = i
            i+=1
        
        return max(maxsub, i-start)
            