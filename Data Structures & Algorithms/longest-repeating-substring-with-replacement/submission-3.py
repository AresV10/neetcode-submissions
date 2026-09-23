class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_freq, left, right= {},0,0
        while right < len(s):
            character_freq[s[right]] = character_freq.get(s[right], 0) + 1
            if right-left+1 - max(character_freq.values()) > k:
                character_freq[s[left]] = character_freq[s[left]] - 1
                left+=1
            right+=1
        return right-left