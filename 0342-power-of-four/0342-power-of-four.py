class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            k=log10(n)/log10(4)
            if type(k)==int or str(k)==str(int(k))+'.0':
                return True
        else:
            return False
        