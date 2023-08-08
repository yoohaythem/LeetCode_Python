class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.append(0)
        count = left = right = 0
        while right < n:
            if nums[right] - nums[left - 1] < k:
                right += 1
            if nums[right] - nums[left - 1] > k:
                left += 1
            else:
                count += 1
                left += 1
                right += 1
        return count
        '''
        '''
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.append(0)
        print(nums)
        count = 0
        for i in range(0, n):
            for j in range(-1, i):
                if nums[i] - nums[j] == k:   # 遍历加判断，就用字典！！！
                    count += 1
        return count
        '''
        count_dict = {0: 1}
        count = 0
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum - k in count_dict:
                count += count_dict[sum - k]
            if sum in count_dict:
                count_dict[sum] += 1
            else:
                count_dict[sum] = 1
        return count
