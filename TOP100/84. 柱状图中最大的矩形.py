class Solution(object):
    def largestRectangleArea1(self, heights):  # 超时
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        result = 0
        for i in range(n):
            if heights[i] == 0:
                continue
            left = right = i
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1
            while right < n - 1 and heights[right + 1] >= heights[i]:
                right += 1
            result = max(result, (right - left + 1) * heights[i])
        return result

    def largestRectangleArea2(self, heights):
        stack = []
        heights.append(0)
        n = len(heights)
        maximum = 0
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                if heights[i] == heights[stack[-1]]:
                    stack.pop()
                    continue
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maximum = max(maximum, height * width)
            stack.append(i)
        return maximum


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea2([0, 1, 0, 1]))
