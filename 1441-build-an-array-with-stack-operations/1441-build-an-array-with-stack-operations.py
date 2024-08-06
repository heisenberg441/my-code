class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        nums=[i for i in range(1,n+1)]
        stack=[]
        res=[]
        i=0
        while i<n and sum(stack)!=sum(target):
            if nums[i]  in target:
                stack.append(nums[i])
                res.append('Push')
            else:
                stack.append(nums[i])
                stack.pop()
                res.append('Push')
                res.append('Pop')
            i+=1
        return res
