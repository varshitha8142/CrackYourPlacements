class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        nums=s
        k=3
        a1=[]
        for i in range(len(nums)-(k-1)):
            x=nums[i:i+k]
            if len(x)==len(set(x)):
                a1.append(x)
        return len(a1)
