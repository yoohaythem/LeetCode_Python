class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indic = {}
        temp = []
        for p in prerequisites:
            if p[1] in indic:
                indic[p[1]].append(p[0])
            else:
                indic[p[1]] = [p[0]]
        for i in range(numCourses):
            if i not in indic:
                temp.append(i)

        while temp:
            for course in indic:
                for t in temp:
                    if t in indic[course]:
                        indic[course].remove(t)
            temp = []
            keymap = indic.keys()
            for course in keymap:
                if not indic[course]:
                    indic.pop(course)
                    temp.append(course)

        return not indic

    def canFinish2(self, numCourses, prerequisites):
        indic = {}
        inlist = [0] * numCourses
        temp = []
        visited = 0

        for p in prerequisites:
            inlist[p[0]] += 1
            if p[1] in indic:
                indic[p[1]].append(p[0])
            else:
                indic[p[1]] = [p[0]]
        for i in range(numCourses):
            if not inlist[i]:
                temp.append(i)

        while temp:
            visited += 1
            clas = temp.pop(0)
            for c in indic.get(clas) or []:
                inlist[c] -= 1
                if not inlist[c]:
                    temp.append(c)

        return visited == numCourses

if __name__ == '__main__':
    s = Solution()
    print(s.canFinish2(2, [[0, 1]]))
