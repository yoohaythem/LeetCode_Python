class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        lst = []
        result = []
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for num in dic:
            lst.append((num, dic[num]))
        lst.sort(key=lambda x: -x[1])
        for i in range(k):
            result.append(lst[i][0])
        return result
