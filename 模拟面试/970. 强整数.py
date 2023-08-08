class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_set = set()
        y_set = set()
        i = j = 0
        res = set()
        while x>1:
            if x ** i < bound:
                x_set.add(x ** i)
            else:
                break
            i += 1
        else:
            x_set = {1}
        while y>1:
            if y ** j < bound:
                y_set.add(y ** j)
            else:
                break
            j += 1
        else:
            y_set = {1}
        print(x_set,y_set)
        for x in x_set:
            for y in y_set:
                if x+y<=bound:
                    res.add(x+y)
        return list(res)