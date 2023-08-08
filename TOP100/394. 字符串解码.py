class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        letter_stack = [""]
        tmp_num = ""
        tmp_letter = ""
        for ch in s:
            if ch.isdigit():
                tmp_num += ch
            elif ch.islower():
                tmp_letter += ch
            elif ch == "[":
                if tmp_num:
                    num_stack.append(tmp_num)
                letter_stack[-1] += tmp_letter
                letter_stack.append("")
                tmp_num = ""
                tmp_letter = ""
            elif ch == "]":
                letter_stack[-1] += tmp_letter
                tmp_letter = ""
                add = letter_stack.pop() * int(num_stack.pop())
                letter_stack[-1] += add
        letter_stack[-1] += tmp_letter
        return letter_stack[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("b2[a2[c]b2[a]]sa"))
