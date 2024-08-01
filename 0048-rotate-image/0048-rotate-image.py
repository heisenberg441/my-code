class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=matrix
        for i in range(1,len(m)):
            for j in range(1,len(m)):
                if i==j :
                    k=j-1
                    l=i-1
                    aux=m[i][k]
                    m[i][k]=m[l][j]
                    m[l][j]=aux
                    while k!=0 and l!=0:
                        l=l-1
                        k=k-1
                        aux=m[i][k]
                        m[i][k]=m[l][j]
                        m[l][j]=aux

        for i in range(len(m)):
            m[i] = m[i][::-1]