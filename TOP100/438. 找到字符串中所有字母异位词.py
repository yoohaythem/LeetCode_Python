class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns = len(s)
        np = len(p)
        if ns < np:
            return []
        dict_p = [0] * 26
        dict_s = [0] * 26
        result = []
        for i in range(np):
            dict_p[ord(p[i]) - ord("a")] += 1
            dict_s[ord(s[i]) - ord("a")] += 1
        if dict_p == dict_s:
            result.append(0)
        for i in range(ns - np):
            dict_s[ord(s[i]) - ord("a")] -= 1
            dict_s[ord(s[i + np]) - ord("a")] += 1
            if dict_p == dict_s:
                result.append(i + 1)
        return result
