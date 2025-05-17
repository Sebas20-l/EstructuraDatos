class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        extra={}
        for i in range(len(nums)):
            tmp= target - nums[i]
            if (tmp in extra):
                return [extra[tmp], i]

            extra[nums[i]]= i
            
nums = [2, 7, 11, 15]
target = 9


sol = Solution()
result = sol.twoSum(nums, target)

print("Output:", result)