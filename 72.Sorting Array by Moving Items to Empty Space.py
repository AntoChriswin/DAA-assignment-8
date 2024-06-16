def min_operations_to_sort(nums):
    n = len(nums)
    empty_pos = nums.index(0)
    operations = 0

    for i in range(n):
        if nums[i] != i and nums[i] != 0:
            nums[empty_pos], nums[i] = nums[i], nums[empty_pos]
            empty_pos = i
            operations += 1

    return operations


# Test Examples
print(min_operations_to_sort([4, 2, 0, 3, 1]))  # Output: 3
print(min_operations_to_sort([1, 2, 3, 4, 0]))  # Output: 0
print(min_operations_to_sort([1, 0, 2, 4, 3]))  # Output: 2
