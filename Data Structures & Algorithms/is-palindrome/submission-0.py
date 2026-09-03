class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = ''.join(ch.lower() for ch in s if ch.isalnum())
        palindrome_length = len(compare)
        for i in range(palindrome_length//2):
            if compare[i] != compare[palindrome_length-1-i]:
                return False

        return True