class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = minimum = result = nums[0]
        for i in range(1, len(nums)):
            tmp = maximum
            maximum = max(nums[i], maximum * nums[i], minimum * nums[i])
            minimum = min(nums[i], tmp * nums[i], minimum * nums[i])
            result = max(result, maximum, minimum)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-4, -3, -2]))
