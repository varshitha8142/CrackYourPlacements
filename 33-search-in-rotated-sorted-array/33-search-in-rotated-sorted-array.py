class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c=nums[:target]+nums[target:]
        if target in nums:
            return c.index(target)
        return -1
        