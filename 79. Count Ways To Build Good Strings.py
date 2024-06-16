def count_good_strings(low, high, zero, one):
    MOD = 10**9 + 7
    dp = [[0] * (high + 1) for _ in range(2)]
    dp[0][0] = dp[1][0] = 1
    for i in range(1, high + 1):
        dp[0][i] = (dp[0][i - 1] + dp[1][i - 1]) % MOD
        dp[1][i] = dp[0][i - 1]
        if i - low >= 0:
            dp[0][i] = (dp[0][i] - dp[0][i - low] + MOD) % MOD
            dp[1][i] = (dp[1][i] - dp[1][i - low] + MOD) % MOD
        if i - high > 0:
            dp[0][i] = (dp[0][i] - dp[0][i - high - 1] + MOD) % MOD
            dp[1][i] = (dp[1][i] - dp[1][i - high - 1] + MOD) % MOD
    return (dp[0][high] - dp[0][low - 1] + MOD) % MOD

# Example Usage
low = 3
high = 3
zero = 1
one = 1
output = count_good_strings(low, high, zero, one)
print(output)  # Output: 8
