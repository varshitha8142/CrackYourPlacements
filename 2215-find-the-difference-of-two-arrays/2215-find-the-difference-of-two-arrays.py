class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x=[];x1=[]
        for i in nums1:
            if i not in nums2:
                x.append(i)
        for i in nums2:
            if i not in nums1:
                x1.append(i)
        return set(x),set(x1)
                
                
                
        