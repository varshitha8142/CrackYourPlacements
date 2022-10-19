class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        A1=arr1
        A2=arr2
        x=[]
        for i in A2:
            if i in A1:
                z=A1.count(i)
                while z!=0:
                    x.append(i)
                    z-=1
                    A1.remove(i)
        return x+sorted(A1)       
        