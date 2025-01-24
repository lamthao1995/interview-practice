#
# Note: The class, method and parameter have been specified. Please do not modify
#
#
#
# @param nums Integer One-dimensional Array
# @return Integer
#
class Solution:
    def minimumMountainRemovals(self, nums):
        # write code here
        left_dp = self.get_LIS(nums)
        nums.reverse()
        right_dp = self.get_LIS(nums)
        right_dp.reverse()
        ans = 0
        n = len(nums)
        for idx in range(1, n - 1):
            ans = max(ans, left_dp[idx] + right_dp[idx] - 1)
        return n - ans

    def get_LIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

def test():
    sol = Solution()
    test_cases = [[1,3,1], [2,1,1,5,6,2,3,1]]
    for nums in test_cases:
        print(sol.minimumMountainRemovals(nums))

test()