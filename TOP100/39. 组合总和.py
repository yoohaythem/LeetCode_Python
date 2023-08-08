import copy


class Solution(object):
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []

        def branch(start, nums, candidates, target):
            for i in range(start, len(candidates)):
                if candidates[i] < target - sum(nums):
                    nums.append(candidates[i])
                    branch(i, nums, candidates, target)
                elif candidates[i] == target - sum(nums):
                    nums.append(candidates[i])
                    result.append(copy.copy(nums))
                    nums.pop()
                    if len(nums) > 0:
                        nums.pop()
                    break
                else:
                    if len(nums) > 0:
                        nums.pop()
                    break
                if i == len(candidates) - 1 and len(nums) > 0:
                    nums.pop()

        branch(0, [], candidates, target)
        return result

    # 杜绝append！
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        result = []

        def branch(temp):
            for i in candidates:
                if len(temp) > 0 and i < temp[-1]:
                    continue
                if i < target - sum(temp):
                    branch(temp + [i])
                elif i == target - sum(temp):
                    result.append(temp + [i])
                else:
                    break

        branch([])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(candidates=[2, 3, 6, 7], target=7))
