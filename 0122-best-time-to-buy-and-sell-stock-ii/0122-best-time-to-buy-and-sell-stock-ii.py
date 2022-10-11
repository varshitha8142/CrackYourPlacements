class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=[]
        for i in range(len(prices)-1):
            if prices[i]>prices[i+1]:
                pass
            else:
                x.append(abs(prices[i]-prices[i+1]))
        return sum(x)