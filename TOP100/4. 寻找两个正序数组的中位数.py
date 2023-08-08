import math


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        l1 = len(nums1)
        l2 = len(nums2)
        length = l1 + l2

        size = math.floor((length + 1) / 2)

        if nums1 == []:
            if length % 2 == 0:
                return (nums2[size - 1] + nums2[size]) / 2
            else:
                return nums2[size - 1]

        i = 0
        while nums1[i] < nums2[size - i - 1]:
            i = i + 1
            if i >= l1:
                break

        if length % 2 == 1:
            if i == 0:
                return nums2[size - 1]
            else:
                return max(nums1[i - 1], nums2[size - i - 1])

        if length % 2 == 0:
            if i == 0:
                if size - i >= l2:
                    return (nums1[i] + nums2[size - i - 1]) / 2
                else:
                    return (min(nums1[i], nums2[size - i]) + nums2[size - i - 1]) / 2
            elif i == l1:
                if size - i - 1 < 0:
                    return (nums1[i - 1] + nums2[size - i]) / 2
                return (max(nums1[i - 1], nums2[size - i - 1]) + nums2[size - i]) / 2
            else:
                return (max(nums1[i - 1], nums2[size - i - 1]) + min(nums1[i], nums2[size - i])) / 2
