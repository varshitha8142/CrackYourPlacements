class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        b,c=[],[]
        for i in range(len(nums)):
            b.append(nums[i])
            c.append(sum(b))
        return c