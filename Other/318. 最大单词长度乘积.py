class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_list = []
        for word in words:
            tmp = 0
            for letter in word:
                tmp |= 1 << (ord(letter) - ord("a"))
            word_list.append((tmp, len(word)))
        maximun = 0
        for i in range(len(word_list) - 1):
            for j in range(i + 1, len(word_list)):
                if word_list[i][0] & word_list[j][0] == 0:
                    maximun = max(maximun, word_list[i][1] * word_list[j][1])
        return maximun