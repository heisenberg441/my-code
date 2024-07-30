class Solution:
    def removeKdigits(self, num: str, k: int) -> str:


        if len(num) == k:
            return '0'
        else:
            i = 1
            stack = [num[0]]
            nb = 0
            while i < len(num) and nb < k:
                if stack and num[i] < stack[-1]:
                    stack.pop()
                    nb += 1
                else:
                    stack.append(num[i])
                    i += 1

            while i < len(num):
                stack.append(num[i])
                i += 1

            while nb < k:
                stack.pop()
                nb += 1


            result = ''.join(stack).lstrip('0')
            return result if result else '0'



