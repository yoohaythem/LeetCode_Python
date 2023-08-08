class Solution(object):
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        results = []
        if digits == "":
            return []
        digits = digits + "1" * (4 - len(digits))
        for i in dicts.get(digits[0]):
            for j in dicts.get(digits[1]):
                for k in dicts.get(digits[2]):
                    for l in dicts.get(digits[3]):
                        results.append(i + j + k + l)
        return results

    def letterCombinations2(self, digits):

        def generator(l1, l2):
            l = []
            if len(l2) == 0:
                return l1
            for i in l1:
                for j in l2:
                    l.append(j + i)
            return l

        dicts = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        results = []

        for i in digits:
            results = generator(dicts[i], results)

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations2("23"))
