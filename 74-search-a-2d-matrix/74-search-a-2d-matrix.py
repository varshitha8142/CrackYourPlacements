class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=[]
        for i in range(len(matrix)):
            m.extend(matrix[i])
        return(target in m)
        