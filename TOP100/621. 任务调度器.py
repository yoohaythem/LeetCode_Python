class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t][0] += 1
            else:
                freq[t] = [1, 1]
        ln = len(tasks)
        time = 0
        for i in range(ln):
            time += 1
            nexttime = min(v[1] for v in freq.values() if v[0] > 0)
            time = max(time, nexttime)
            m = max(v[0] for v in freq.values() if v[1] <= time)
            for key in freq:
                if freq[key][0] == m and freq[key][1] <= time:
                    freq[key][0] -= 1
                    freq[key][1] = time + n + 1
                    break
        return time
