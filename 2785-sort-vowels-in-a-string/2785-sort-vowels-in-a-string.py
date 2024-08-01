class Solution:
    def sortVowels(self, s: str) -> str:
        v=['a','e','i','o','u']
        l=[]
        s=list(s)
        for char in s:
            if char.lower() in v:
                l.append(char)
        l.sort(reverse=True)
        print(l)
        for i in range(len(s)):
            if s[i].lower() in v:
                s[i]=l.pop()
        return ''.join(s)
                
