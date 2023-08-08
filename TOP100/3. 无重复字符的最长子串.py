class Solution(object):

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0
        length = 1
        for i in range(len(s) - 1):
            if len(s) - i <= length:
                break
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    if j - i > length:
                        length = j - i
                        break
                    else:
                        break
                if j == len(s) - 1:
                    length = len(s) - i
        return length

    def lengthOfLongestSubstring2(self, s):
        length = 0
        for i in range(0, len(s)):
            if len(s) - i <= length:
                break
            for j in range(i + 1, len(s) + 1):
                if j == len(s) or s[j] in s[i:j]:
                    length = max(j - i, length)
                    break
        return length

    def lengthOfLongestSubstring3(self, s):
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i >= n - ans:
                break
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


if __name__ == '__main__':
    from datetime import time

    s = Solution()
    # start = time.process_time()
    print(s.lengthOfLongestSubstring1("123456789012"))
    # end = time.process_time()
    # print(end - start)
