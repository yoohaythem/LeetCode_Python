class Solution(object):

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums, target):
        l = len(nums)
        hashtable = dict()
        for i in range(l):
            if target - nums[i] in hashtable.keys():
                return [hashtable.get(target - nums[i]), i]
            hashtable[nums[i]] = i
            # print(hashable)
        return []

    def twoSum3(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum2([11, 2, 7, 15], 9))
