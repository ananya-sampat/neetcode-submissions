class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            if num not in x:
                x.add(num)
            else:
                return True
        return False
        