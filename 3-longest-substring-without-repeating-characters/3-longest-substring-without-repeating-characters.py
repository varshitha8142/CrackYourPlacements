class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        nums=s
        b=""
        c=0
        x=[]
        i=0;j=len(nums)-1
        while i<=j:
            if nums[i] not in b:
                b+=nums[i]
                i+=1
            elif nums[i] in b:
                x.append(len(b))
                c+=1
                i=c
                b=""
        if len(b)!=0:
            x.append(len(b))
        if len(x)!=0:
            return max(x)
        return 0
