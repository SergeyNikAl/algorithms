# ID: 72633490

def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        left_num = nums[left]
        if left_num == target:
            return left
        right_num = nums[right]
        if right_num == target:
            return right
        mid = (left + right) // 2
        pivot = nums[mid]
        if target == pivot:
            return mid
        if left_num < pivot:
            if left_num < target < pivot:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if pivot < target < right_num:
                left = mid + 1
            else:
                right = mid - 1
    return -1
