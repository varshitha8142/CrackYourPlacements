class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        a=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=x:
                a.append(True)
            else:
                a.append(False)
        return a
            