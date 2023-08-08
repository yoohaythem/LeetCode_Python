class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        n = len(street)
        s = set()
        for i in range(n):
            if street[i] == "H":
                if i - 1 in s:
                    continue
                if i < n - 1 and street[i + 1] == ".":
                    s.add(i + 1)
                elif i and street[i - 1] == ".":
                    s.add(i - 1)
                else:
                    return -1
        return len(s)

