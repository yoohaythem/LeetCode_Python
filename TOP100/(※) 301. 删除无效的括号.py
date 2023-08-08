class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        lremove = rremove = 0
        for ch in s:
            if ch == "(":
                lremove += 1
            elif ch == ")":
                if lremove:
                    lremove -= 1
                else:
                    rremove += 1

        def isValid(str):
            count = 0
            for ch in str:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                    if count < 0:
                        return False
            return not count

        def helper(s, start, lremove, rremove):
            if not lremove and not rremove and isValid(s):
                result.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if lremove + rremove > len(s) - i:
                    break
                if lremove > 0 and s[i] == "(":
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove)
                if rremove > 0 and s[i] == ")":
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1)

        helper(s, 0, lremove, rremove)
        return result

    def removeInvalidParentheses2(self, s):
        def isValid(str):
            count = 0
            for ch in str:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                    if count < 0:
                        return False
            return not count

        result = []
        currSet = {s}
        while True:
            for ele in currSet:
                if isValid(ele):
                    result.append(ele)
            if result:
                return result
            nextSet = set()
            for ele in currSet:
                for i in range(len(ele)):
                    if i > 0 and ele[i] == ele[i - 1]:
                        continue
                    if ele[i] == "(" or ")":
                        nextSet.add(ele[:i] + ele[i + 1:])
            currSet = nextSet


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses(")()("))
