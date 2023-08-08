class Solution(object):
    def merge1(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = []
        temp = intervals[0]
        for i in range(len(intervals)):
            if intervals[i][0] <= temp[1]:
                temp = [temp[0], max(intervals[i][1], temp[1])]
            else:
                result.append(temp)
                temp = intervals[i]
            if i == len(intervals) - 1:
                result.append(temp)
        return result


    def merge2(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
