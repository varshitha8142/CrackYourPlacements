class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x={}
        for i in arr:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        return(len(set(x.values())))==len(x.values())