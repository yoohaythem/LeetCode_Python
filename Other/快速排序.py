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
    sort(nums, l, left - 1)
    sort(nums, left + 1, r)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sort(nums, 0, len(nums) - 1)
print(nums)
