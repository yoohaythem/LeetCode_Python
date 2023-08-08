class Solution(object):
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = [[]]
        # for i in nums:
        #     n = len(result)
        #     r = 0
        #     while r < n:
        #         result.append(result[r] + [i])
        #         r += 1
        # return result
        result = [[]]
        for i in nums:
            for r in range(len(result)):
                result.append(result[r] + [i])
                r += 1
        return result

    def subsets2(self, nums):
        result = []
        for i in range(2 ** len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & (1 << j) != 0:  # 掩码法
                    temp.append(nums[j])
            result.append(temp)

        return result

    def subsets3(self, nums):
        result = []
        n = len(nums)

        def traceback(start, k, temp):
            if k == 0:
                result.append(temp + [])
                return
            for i in range(start, n):
                temp.append(nums[i])
                traceback(i + 1, k - 1, temp)
                temp.pop()

        for i in range(n + 1):
            traceback(0, i, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets3([1, 2, 3]))
