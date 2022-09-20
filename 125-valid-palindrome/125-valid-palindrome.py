class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        a=""
        for i in s:
            i=i.lower()
            if ord(i) in list(range(97,122)) or ord(i) in list(range(48,58)):
                x+=i
                a=i+a
        if x==a:
            return True
        else:
            return False