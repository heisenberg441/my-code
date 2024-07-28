class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        else:
            d={')':'(',']':'[','}':'{'}
            stack=[]
            for elem in s:
                if elem not in d or len(stack)==0 or d[elem]!=stack[-1]:
                    stack.append(elem)
                elif d[elem]==stack[-1]:
                    stack.pop()
            if stack :
                return False
            else:
                return True