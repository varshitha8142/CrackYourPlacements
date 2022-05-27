class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        x=[]
        i=1
        while(i!=target[-1]+1):
            if i in target:
                x.append("Push")
                i+=1
            else:
                x.append("Push")
                x.append("Pop")
                i+=1
        return x
        