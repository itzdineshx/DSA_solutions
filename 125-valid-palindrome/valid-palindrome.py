class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "".join(c.lower() for c in s if c.isalnum())
        return r == r[::-1]