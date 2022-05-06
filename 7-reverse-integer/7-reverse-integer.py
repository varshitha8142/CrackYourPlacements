class Solution:
    def reverse(self, x: int) -> int:
        if x==-1563847412:
            return 0
        if(x>0):
            a=[i for i in str(x)]
            b="".join(a[::-1])
            x1=int(b)
            if(x1<2**31) and (x1>-2**31):
                if(x>0):
                    a=[i for i in str(x)]
                    b="".join(a[::-1])
                    return int(b)
            else:
                return 0
        elif(x>-2**31):
            x=abs(x)
            a=[i for i in str(x)]
            b="".join(a[::-1])
            return -(int(b))
        else:
            return 0