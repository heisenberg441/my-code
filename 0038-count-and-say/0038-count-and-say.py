class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x="1"
        for i in range(2,n+1):
            j=0
            ch=""
            while(j<len(x)):
                    k=j
                    nb=0
                    test=True
                    while(k<len(x)and test):
                            if x[j]==x[k]:
                                nb=nb+1
                            else:
                                test=False
                            k=k+1
                    ch=ch+str(nb)+x[j]
                    j=j+nb
            print(ch)
            x=ch
        return x
                
        