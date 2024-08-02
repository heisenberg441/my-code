class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(target, row):
            left, right = 0, len(matrix[row]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        if len(matrix)==1:
            return binary_search(target,0)
        else:
            for i in range(len(matrix)):
                if target<matrix[i][0]:
                    return binary_search(target,i-1)
                if target==matrix[i][0]:
                    return True 
            return binary_search(target,len(matrix)-1)