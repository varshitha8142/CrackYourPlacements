class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d={};d1={};c=0
        for i in words1:
            d[i]=d.get(i,0)+1
        for i,j in list(d.items()):
            if j>1 :
                del d[i]
        for i in words2:
            d1[i]=d1.get(i,0)+1
        for i,j in list(d1.items()):
            if j>1 :
                del d1[i]
        for i in d:
            if i in d1:
                c+=1
        return c