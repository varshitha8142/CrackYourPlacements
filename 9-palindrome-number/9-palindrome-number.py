class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
           print('false')
        else:
            a=str(x)
            return(a==a[::-1])