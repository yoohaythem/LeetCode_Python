class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxarea = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                maxarea = max(maxarea, (j - i) * min(height[i], height[j]))
        return maxarea

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        result = 0
        while right > left:
            result = max((right - left) * min(height[left], height[right]), result)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea2([2, 3, 4, 5, 18, 17, 6]))
