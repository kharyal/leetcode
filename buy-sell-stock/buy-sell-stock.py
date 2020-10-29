class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        is_bought = False
        bought_for = 0
        for i in range(len(prices)):
            if i<len(prices)-1:
                if prices[i+1]>prices[i]:
                    if is_bought:
                        continue
                    else:
                        # print(prices[i])
                        is_bought = True
                        bought_for = prices[i]

                else:
                    if is_bought:
                        # print(prices[i])
                        is_bought = False
                        ret = ret + prices[i] - bought_for
                    else:
                        continue
            
            else:
                if is_bought:
                    ret = ret + prices[i] - bought_for
        return ret

sol = Solution()
print(sol.maxProfit([1,2,3,4,5]))