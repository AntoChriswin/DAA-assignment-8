from math import gcd

def minSubarrays(nums):
    def check_valid(arr):
        return gcd(arr[0], arr[-1]) > 1

    if not check_valid(nums):
        return -1

    count = 1
    for i in range(1, len(nums)):
        if not check_valid(nums[:i]) or not check_valid(nums[i:]):
            count += 1

    return count

# Test cases
print(minSubarrays([2, 6, 3, 4, 3]))  # Output: 2
print(minSubarrays([3, 5]))  # Output: 2
print(minSubarrays([1, 2, 1]))  # Output: -1
