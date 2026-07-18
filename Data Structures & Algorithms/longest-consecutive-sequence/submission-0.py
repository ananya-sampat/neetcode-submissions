class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        max_seq = 1
        current_seq = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                current_seq += 1
            else:
                current_seq = 1

            max_seq = max(max_seq, current_seq)

        return max_seq
            

            