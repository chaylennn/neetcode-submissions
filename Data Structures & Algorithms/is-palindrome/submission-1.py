class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [i for i in s[::-1] if i.isalnum()]
        y = [i for i in s if i.isalnum()]
        print(str(x).lower())
        print(str(y).lower())
        return str(x).lower() == str(y).lower()