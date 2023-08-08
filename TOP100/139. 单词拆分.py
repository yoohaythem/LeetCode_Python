class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        '''
        temp = []
        count = 0
        for i in s:
            if len(temp) == 0:
                for word in wordDict:
                    if word[0] == i:
                        temp.append(word)
                if len(temp) == 0:
                    return False
                count = 1
            else:
                for word in temp:
                    if count == len(word):
                        if self.wordBreak(s[count:], wordDict):
                            return True
                    if word[count] != i:
                        temp.remove(word)
                    if len(temp) == 0:
                        return False
                count += 1
        return True
        '''
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        for i in range(1, len(s) + 1):  # i:字符串第i个字符
            for j in range(i):
                # if result[j] and (s[j:i] if i < len(s) else s[j:]) in wordDict:
                if result[j] and s[j:i] in wordDict:
                    result[i] = True
                    break
        return result[-1]

    def wordBreak2(self, s, wordDict):
        if not s:
            return True
        breakp = [0]
        for i in range(len(s) + 1):
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        return breakp[-1] == len(s)
