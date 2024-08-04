class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()  
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            x = nums[i]
            goal = -x
            l, r = i + 1, len(nums) - 1 
            processed = set()  
            while r > l:
                if nums[l] in processed:
                    l += 1
                    continue
                if nums[r] in processed:
                    r -= 1
                    continue
                s = nums[l] + nums[r]
                if s == goal:
                    result.add((x, nums[l], nums[r]))
                    processed.add(nums[l])
                    processed.add(nums[r])
                    l += 1
                    r -= 1
                elif s > goal:
                    r -= 1
                else:
                    l += 1
        return [list(triplet) for triplet in result]