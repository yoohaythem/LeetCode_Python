class Solution(object):
    def minWindow1(self, s, t):  # 超时
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            if s[i] in t:
                temp = t.replace(s[i], "", 1)
                for j in range(i + 1, len(s) + 1):
                    if len(temp) == 0:
                        str = s[i:j] if j < len(s) else s[i:]
                        if result == "" or len(result) > len(str):
                            result = str
                        break
                    if j == len(s):
                        return result
                    if s[j] in temp:
                        temp = temp.replace(s[j], "", 1)
        return result

    def minWindow2(self, s, t):
        left = right = 0
        n = len(s)
        dict = {}
        result = ""
        for c in t:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        while right < n:
            if len(list(filter(lambda x: x > 0, dict.values()))) == 0:
                if result == "" or right - left < len(result):
                    result = s[left:right]
                dict[s[left]] += 1
                left += 1
            while left < n - 1 and (s[left] not in dict or dict[s[left]] < 0):
                if s[left] in dict and dict.get(s[left]) < 0:
                    dict[s[left]] += 1
                left += 1
                if right < left:
                    right = left
            if s[right] in dict:
                dict[s[right]] -= 1
            right += 1

        if len(list(filter(lambda x: x > 0, dict.values()))) == 0:
            while s[left] not in t or dict[s[left]] < 0:
                if s[left] in dict and dict.get(s[left]) < 0:
                    dict[s[left]] += 1
                left += 1
            if result == "" or right - left < len(result):
                result = s[left:]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow2(s="BBAAC", t="ABA"))
