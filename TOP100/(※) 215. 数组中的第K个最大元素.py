class Solution(object):
    def findKthLargest(self, nums, k):
        def sort(nums, left, right):
            l, r = left, right
            if right <= left:
                return
            pivot = nums[l]
            p = right
            while left != right:
                if p == right:
                    if nums[p] > pivot:
                        nums[left] = nums[right]
                        left += 1
                        p = left
                    else:
                        right -= 1
                        p = right
                elif p == left:
                    if nums[p] > pivot:
                        left += 1
                        p = left
                    else:
                        nums[right] = nums[left]
                        right -= 1
                        p = right
            nums[left] = pivot
            if left > k - 1:
                sort(nums, l, left - 1)
            elif left < k - 1:
                sort(nums, left + 1, r)

        sort(nums, 0, len(nums) - 1)
        # print(nums)
        return nums[k - 1]




if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 4, 2, 6, 8, 12, 78, 6, 9, 5, 7], 10))
