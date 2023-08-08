class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        vote = "start"
        for num in nums:
            if count == 0:
                vote = num
                count += 1
                continue
            if num == vote:
                count += 1
            else:
                count -= 1
        return vote

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
'''
