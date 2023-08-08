import collections


class Solution(object):
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        index_list = []
        result = []
        for word in strs:
            letter_dict = {}
            index = ""
            for ch in word:
                if ch not in letter_dict:
                    letter_dict[ch] = 1
                else:
                    letter_dict[ch] += 1
            if letter_dict not in index_list:
                index_list.append(letter_dict)
                result.append([word])
            else:
                result[index_list.index(letter_dict)].append(word)

        return result

    def groupAnagrams2(self, strs):
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

    def groupAnagrams3(self, strs):
        mp = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in mp:
                mp[key] = [str]
            else:
                mp[key].append(str)

        return mp.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams3(["ems", "mes"]))
