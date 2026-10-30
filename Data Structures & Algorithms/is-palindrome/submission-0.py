class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(palind.lower() for palind in s if palind.isalnum())
        rev = clean[::-1]
        return clean == rev