class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x=0
        mul=0
        for i in range(len(num2)-1,-1,-1):
            r=0
            s=""
            for j in range(len(num1)-1,-1,-1):
                res=int(num2[i])*int(num1[j])+r
                if res>=10 and j!=0:
                    r=res//10
                    res=res%10
                    
                else:
                    r=0
                s=str(res)+s
            s=s+'0'*x
            mul=mul+int(s)
            x=x+1
        return str(mul)
