class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temperatures[stack.pop()] = i - stack[-1]
            stack.append(i)
        for num in stack:
            temperatures[num] = 0
        return temperatures
