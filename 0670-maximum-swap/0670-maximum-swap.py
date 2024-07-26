class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        z=num
        max=str(num)
        num=list(str(num))
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                aux=num[i]
                num[i]=num[j]
                num[j]=aux
                x=''.join(num)
                print(x,z)
                if x>max:
                    max=x
                aux=num[i]
                num[i]=num[j]
                num[j]=aux
        return int(max)