class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        m = len(goal)
        if m != n:
            return False
        l = []
        repeat = 0
        for i in range(n):
            if s[i] != goal[i]:
                l.append(i)
            if not repeat and s[i] in s[:i]:
                repeat = 1
        if not l and repeat or len(l) == 2 and s[l[0]] == goal[l[1]] and s[l[1]] == goal[l[0]]:
            return True
        return False