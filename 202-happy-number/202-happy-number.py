class Solution:
    def isHappy(self, n: int) -> bool:
        b=n
        c=0
        while(b!=1):
            b=[int(i)*int(i) for i in str(b)]
            b=sum(b)
            c+=1
            if(c>90):
                return(False)
        else:
            return(True)
