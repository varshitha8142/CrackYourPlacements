class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            i=i.lower()
            if ord(i) in list(range(97,122)) or ord(i) in list(range(48,58)):
                x+=i
        if x==x[::-1]:
            return True
        else:
            return False