class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        j=0
        x=[]
        for i in candies:
            candies[j]=i+extraCandies
            if max(candies)==candies[j]:
                x.append(True)
            else:
                x.append(False)
            candies[j]=candies[j]-extraCandies
            j+=1
        return x
            