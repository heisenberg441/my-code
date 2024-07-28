class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={0:-1}
        s=0
        for i,num in enumerate(nums):
            s+=num
            r=s%k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>1:
                return True
        return False
