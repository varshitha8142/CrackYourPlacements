class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices)<2:
            return 0
        max_pr=0
        min_buy=prices[0]
        for i in prices[1:]:
            max_pr=max(max_pr,i-min_buy)
            min_buy=min(min_buy,i)
        return max_pr
