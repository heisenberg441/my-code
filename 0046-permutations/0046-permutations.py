class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        for i in range(len(nums)):
            l=[]
            for perm in perms:
                x = perm.copy()
                b=x.copy()
                for j in range(i+1):
                    x.insert(j, nums[i])
                    l.append(x)
                    x=b.copy()
                perms=l

        return l