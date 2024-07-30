class Solution:
    def romanToInt(self, s: str) -> int:
        add={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sub={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        stack=[s[0]]
        res=add[s[0]]
        for i in range(1,len(s)):
            if stack[-1]+s[i] not in sub:
                stack.append(s[i])
                res+=add[s[i]]
            else:
                res-=add[stack[-1]]
                res+=sub[stack[-1]+s[i]]
                stack.append(s[i])
        return(res)
        
