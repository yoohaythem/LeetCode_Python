class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        top = []
        volume = 0
        for i in range(0, len(height)):
            if height[i] >= (height[i - 1] if i > 0 else 0) and height[i] >= (
            height[i + 1] if i < len(height) - 1 else 0):
                top.append(i)

        def cut(top):
            n = len(top)
            if n > 2:
                j = 1
                while j < len(top) - 1:
                    if height[top[j]] <= height[top[j - 1]] and height[top[j]] <= height[top[j + 1]]:
                        top.pop(j)
                        j = j - 1
                    j = j + 1
                if len(top) != n:
                    cut(top)

        cut(top)

        for h in range(len(top) - 1):
            m = min(height[top[h]], height[top[h + 1]])
            for i in range(top[h] + 1, top[h + 1]):
                volume = volume + (m - height[i] if m - height[i] > 0 else 0)
        return volume


if __name__ == '__main__':
    s = Solution()
    print(s.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]))
