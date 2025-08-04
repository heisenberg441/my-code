class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=height
        i=0
        j=len(a)-1
        m=min(a[i],a[j])*(j-i)
        while i<j:
            if a[i]<a[j]:
                i=i+1
            else:
                j=j-1
            
            m=max(min(a[i],a[j])*(j-i),m)

        return m