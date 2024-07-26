class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_single(nums, start):
                if start == len(nums) - 1:
                    return nums[start]
                return nums[start] ^ find_single(nums, start + 1)
            
        return find_single(nums, 0)