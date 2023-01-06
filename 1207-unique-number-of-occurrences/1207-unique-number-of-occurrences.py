class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x=[]
        for i in set(arr):
            x.append(arr.count(i))
        return((len(set(x)))==len(x))