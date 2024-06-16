def maxSumOfDistinctSubarrays(nums, k):
    if len(set(nums)) < k:
        return 0

    max_sum = 0
    for i in range(len(nums) - k + 1):
        if len(set(nums[i:i + k])) == k:
            max_sum = max(max_sum, sum(nums[i:i + k]))

    return max_sum


# Example 1
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maxSumOfDistinctSubarrays(nums, k))  # Output: 15

# Example 2
nums = [4, 4, 4]
k = 3
print(maxSumOfDistinctSubarrays(nums, k))  # Output: 0
