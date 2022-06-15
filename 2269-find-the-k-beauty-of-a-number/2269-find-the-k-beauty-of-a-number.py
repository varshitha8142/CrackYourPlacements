class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a1=0
        for i in range(len(str(num))-(k-1)):
            num1=str(num)
            a=num1[i:i+k]
            if int(a)!=0:
                if(num%int(a))==0:
                    a1+=1
        return a1
        