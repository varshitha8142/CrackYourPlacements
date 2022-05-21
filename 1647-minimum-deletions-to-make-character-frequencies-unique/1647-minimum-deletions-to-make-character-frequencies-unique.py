from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        x=[]
        c=0
        a=Counter(s)
        for i,j in a.items():
            x.append(j)
        i=0
        z=((len(set(x))+x.count(0))-1)!=(len(x))
        while(len(x)!=len(set(x))) and z:
            z=((len(set(x))+x.count(0))-1)!=(len(x))
            if x.count(x[i])>1 :
                if x[i]!=0:
                    x[i]-=1
                    c+=1
            i+=1
            if(i==len(x)-1):
                i=0
        return(c)


