class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=0
        for i in grid:
            a=[j for j in i if j<0]
            x+=len(a)
        return x