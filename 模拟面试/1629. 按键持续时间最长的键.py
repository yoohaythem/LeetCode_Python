class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        count = {}
        n = len(keysPressed)
        for i in range(n):
            ch = keysPressed[i]
            diff = releaseTimes[i] - releaseTimes[i - 1] if i else releaseTimes[i]
            count[ch] = max(count.get(ch, 0), diff)
        result = max(count.items(), key=lambda x: (x[1], x[0]))
        return result[0]
