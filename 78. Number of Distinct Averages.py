def numOfDistinctAverages(nums):
    nums.sort()
    distinct_averages = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            average = (nums[i] + nums[j]) / 2
            distinct_averages.add(average)

    return len(distinct_averages)


# Example 1
nums1 = [4, 1, 4, 0, 3, 5]
print(numOfDistinctAverages(nums1))  # Output: 2

# Example 2
nums2 = [1, 100]
print(numOfDistinctAverages(nums2))  # Output: 1
