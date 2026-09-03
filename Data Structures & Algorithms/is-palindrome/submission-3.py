class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        palindrome_length = len(s)
        for i in range(palindrome_length//2):
            if s[i] != s[palindrome_length-1-i]:
                return False

        return True