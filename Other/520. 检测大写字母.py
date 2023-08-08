class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 大写1，小写0
        l = []
        for c in word:
            if ord(c) in range(65, 91):  # 65-90
                l.append(1)
            if ord(c) in range(97, 123):  # 97-122
                l.append(0)
        if not sum(l):
            return True
        if l[0] == 1:
            if sum(l) == 1 or sum(l) == len(l):
                return True
        return False

    def detectCapitalUse2(self, word):
        return word.islower() or word.isupper() or word.istitle()
