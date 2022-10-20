class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        x=[]
        for i in matrix:
            x.extend(i)
        x=(sorted(x))
        return x[k-1]
        