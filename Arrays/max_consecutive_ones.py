class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        most = 0
        i = 0

        while i < n:
            count = 0
            while i < n and nums[i] != 0:
                count += 1
                i += 1

            most = max(count, most)
            i += 1

        return most

nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))