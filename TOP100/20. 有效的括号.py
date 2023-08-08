class Solution(object):
    def isValid(self, s):
        l = []
        dict = {
            "{":"}",
            "[":"]",
            "(":")"}
        for i in s:
            if i in dict.keys():
                l.append(dict[i])
            elif len(l) == 0 or i != l[-1]:
                return False
            elif i == l[-1]:
                l.pop()

        # not l
        if len(l) == 0:
            return True
        else:
            return False