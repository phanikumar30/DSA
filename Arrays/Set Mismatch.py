class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mapping=[0]*n

        for i in nums:
            mapping[i-1]+=1

        dup=0
        miss=0
        for i in range(n):
            if mapping[i]==0:
                miss=i+1
            if mapping[i]==2:
                dup=i+1
        return [dup,miss]

nums=[1,2,2,4]
print(Solution().findErrorNums(nums))