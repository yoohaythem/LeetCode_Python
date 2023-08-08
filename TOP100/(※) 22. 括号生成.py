from functools import lru_cache


class Solution(object):
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generator(l1, l2):
            l = []
            if len(l2) == 0:
                return l1
            for i in l1:
                for j in l2:
                    l.append(j + i)
            return l

        result = []
        temp = []
        for i in range(2 * n):
            temp = generator(["(", ")"], temp)

        for char in temp:
            left = right = n
            for i in char:
                if i == "(":
                    left = left - 1
                else:
                    right = right - 1
                if left > right or left < 0:
                    break
            if left > right or left < 0:
                continue
            result.append(char)

        return result

    def generateParenthesis2(self, n):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    def generateParenthesis2_2(self, n):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + "(", left + 1, right)
            if right < left:
                backtrack(S + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans

    @lru_cache(None)
    def generateParenthesis3(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis3(c):
                for right in self.generateParenthesis3(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis3(3))
