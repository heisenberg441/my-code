class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def prefix(words):
            prefix=[0]*len(words)
            vowels=['a','e','i','o','u']
            for i in range(len(words)):
                nb=0
                if words[i][0] in vowels and words[i][-1] in vowels:
                        nb+=1
                if i==0:
                    prefix[i]=nb
                else:
                    prefix[i]=prefix[i-1]+nb
            return(prefix)
        p=prefix(words)
        l=[]
        for i in range(len(queries)):
            d=queries[i][0]
            f=queries[i][1]
            if d>0:
                l.append(p[f]-p[d-1])
            else:
                l.append(p[f])
        return l