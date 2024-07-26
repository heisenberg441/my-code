class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        l=list(d.keys())
        v=list(d.values())
        for i in range(len(v)-1):
            p=i
            for j in range(i+1,len(v)):
                if v[j]>v[p]:
                    p=j
            v[i],v[p]=v[p],v[i]
            l[i],l[p]=l[p],l[i]
        s=""
        for i in range(len(l)):
            s+=l[i]*v[i]
        return(s)
