class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        tmp = []
        for i in range(1, n):
            for j in range(i):
                tmp.append((float(arr[j]) / float(arr[i]), arr[j], arr[i]))
        tmp.sort(key=lambda x: x[0])
        return tmp[k - 1][1], tmp[k - 1][2]
