#class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)):
#            needed = target - nums[i]
#            for j in range(i+1,len(nums)):
#                if nums[j] == needed:
#                    return [i, j]

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[nums[i]] = i