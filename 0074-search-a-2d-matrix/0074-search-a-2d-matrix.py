class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=[]
        for i in matrix:
            x.extend(i)
        return target in x
        