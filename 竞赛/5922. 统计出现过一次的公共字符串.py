class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dict1 = {}
        dict2 = {}
        count = 0
        for word in words1:
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
        for word in words2:
            if word in dict2:
                dict2[word] += 1
            else:
                dict2[word] = 1
        for word in dict1:
            if dict1.get(word) == 1 and dict2.get(word) == 1:
                count += 1
        return count