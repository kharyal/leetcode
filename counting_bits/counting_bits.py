class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = [0]
        highest2pow = 1
        next_highest2pow = 2
        for number in range(1, num+1):
            if number == 1:
                arr.append(1)
            elif number == 2:
                arr.append(1)
                highest2pow = 2
                next_highest2pow = highest2pow*2
            else:
                # print(number, number%highest2pow)
                arr.append(arr[number%highest2pow]+arr[highest2pow])

                if number%next_highest2pow == 0:
                    highest2pow = next_highest2pow
                    next_highest2pow = highest2pow*2
        return arr

sol = Solution()
print(sol.countBits(0))