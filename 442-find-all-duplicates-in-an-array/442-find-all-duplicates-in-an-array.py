from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x=[]
        for i,j in Counter(nums).items():
            if(j>=2):
                x.append( i)
        return x