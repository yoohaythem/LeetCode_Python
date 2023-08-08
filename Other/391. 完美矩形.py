class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # dict = defaultdict(int)
        dict = {}
        area = 0
        for rectangle in rectangles:
            area += (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])
            if (rectangle[0], rectangle[1]) in dict:
                dict[(rectangle[0], rectangle[1])] += 1
            else:
                dict[(rectangle[0], rectangle[1])] = 1
            if (rectangle[0], rectangle[3]) in dict:
                dict[(rectangle[0], rectangle[3])] += 1
            else:
                dict[(rectangle[0], rectangle[3])] = 1
            if (rectangle[2], rectangle[1]) in dict:
                dict[(rectangle[2], rectangle[1])] += 1
            else:
                dict[(rectangle[2], rectangle[1])] = 1
            if (rectangle[2], rectangle[3]) in dict:
                dict[(rectangle[2], rectangle[3])] += 1
            else:
                dict[(rectangle[2], rectangle[3])] = 1
        count = 0
        xmax = ymax = float("-inf")
        xmin = ymin = float("inf")
        for i in dict.items():
            if i[1] == 1:
                count += 1
                xmax = max(xmax, i[0][0])
                xmin = min(xmin, i[0][0])
                ymax = max(ymax, i[0][1])
                ymin = min(ymin, i[0][1])
            elif i[1] % 2:
                return False
        if count == 4 and area == (ymax - ymin) * (xmax - xmin):
            return True
        return False
