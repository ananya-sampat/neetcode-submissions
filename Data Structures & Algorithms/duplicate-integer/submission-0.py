#class Solution:
#    def hasDuplicate(self, nums: List[int]) -> bool:
#        unique_list = [nums[0]]
#        for i in nums[1:]:
#            for j in unique_list:
#                if i == j:
#                    return True
#            unique_list.append(i)
#        return False

##using hash tables
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
