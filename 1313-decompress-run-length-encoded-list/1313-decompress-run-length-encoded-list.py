class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        x=[]
        i=0
        while(i<len(nums)):
            freq,val=nums[i],nums[i+1]
            while(freq>0):
                x.append(val)
                freq-=1
            i+=2
        return x
        
        