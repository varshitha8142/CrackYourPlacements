class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n>0:
            x=log10(n)/log10(3)
            if type(x)==int or str(x)==str(int(x))+'.0':
                return True
        else:
            return False