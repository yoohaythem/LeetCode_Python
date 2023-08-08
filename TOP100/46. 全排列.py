import copy


class Solution(object):
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def append(l1, l2):  # l1:[], l2:[][]
            l = []
            if len(l2) == 0:
                for i in l1:
                    l.append([i])
                return l

            for i in l1:
                for j in l2:
                    temp = copy.copy(j)
                    if i not in j:
                        temp.append(i)
                        l.append(temp)
            return l

        for i in range(len(nums)):
            results = append(nums, results)

        return results

    def permute2(self, nums):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute2([1, 2, 3]))
