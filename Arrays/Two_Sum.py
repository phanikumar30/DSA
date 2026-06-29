class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums and nums.index(diff)!=i:
                return(i,nums.index(diff))                
nums=[6,5,8,1,9]
target=9
print(Solution().twoSum(nums,target))