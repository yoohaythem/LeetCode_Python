import copy


class Solution(object):
    def threeSum1(self, nums):

        negatives = []
        positives = []
        results = []
        resultscheck = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])

        for c in negatives:
            tempnums1 = copy.copy(nums)
            tempnums1.remove(c)
            for b in tempnums1:
                tempnums2 = copy.copy(tempnums1)
                tempnums2.remove(b)
                if -b - c in tempnums2 and {b, c, -b - c} not in resultscheck:
                    resultscheck.append({b, c, -b - c})
                    results.append([b, c, -b - c])
        return results

    def threeSum2(self, nums):
        results = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i, n - 1):
                for k in range(j, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results

    def threeSum3(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left = left + 1
                if sum > 0:
                    right = right - 1
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right:
                        left = left + 1
                        if nums[left] != nums[left - 1]:
                            break
        return result
