# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-31 10:34:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-29 23:17:15
# @Email: liangchaowu5@gmail.com

# method 1,binary search
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix) == 0 or len(matrix[0])==0: return False 
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            if matrix[i][0] > target:
                break
            if matrix[i][0]<= target <= matrix[i][-1] and self.binary_search(matrix, i, target):
                return True
        return False
        
    def binary_search(self, matrix, row, target):
        left, right = 0, len(matrix[row])-1
        while left < right:
            mid = (left+right)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid -1 
            else:
                left = mid + 1
        if left == right:
            return matrix[row][left] == target


# method 2, faster than method 1
# compare the number on the  top right corner with target 
# if equal, return True
# else delete a row or column each time 
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
        