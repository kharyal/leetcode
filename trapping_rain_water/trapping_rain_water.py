class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water1 = [0]
        water2 = [0]
        ret = 0

        if len(height)==0:
            return ret
        max_h = height[0]
        for i in range(1,len(height)):
            if height[i]<max_h:
                water1.append(max_h - height[i])
            else:
                max_h = height[i]
                water1.append(0)
        
        max_h = height[-1]
        for i in range(len(height)-2, -1, -1):
            if height[i]<max_h:
                water2.append(max_h - height[i])
            else:
                max_h = height[i]
                water2.append(0)
        # print(water1)
        # print(water2)
        for i in range(len(height)):
            ret = ret+min(water1[i], water2[len(height)-i-1])
        
        return ret

soln = Solution()
print(soln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))