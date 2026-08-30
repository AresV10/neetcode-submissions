class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_hash = {}
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c)-ord('a')] += 1
            sign = tuple(counts)
            frequency_hash.setdefault(sign, []).append(word)
        return list(frequency_hash.values())