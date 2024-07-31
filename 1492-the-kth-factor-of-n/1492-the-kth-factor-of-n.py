class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=1
        s=[]
        while i<=n:
            print(i)
            if n%i==0:
                s.append(i)
            if len(s)==k:
                return s[-1]
            i+=1
        return -1