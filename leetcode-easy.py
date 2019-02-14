'''
598. Range Addition II
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
'''

def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_m = m
        min_n = n
        for i in ops:
            if i[0] < min_m:
                min_m = i[0]
            if i[1] < min_n:
                min_n = i[1]
        return min_m * min_n

  """
  728. Self Dividing Numbers
  给定范围[left, right]，找出其中所有能被自己各位数字整除的数。
  Input: left = 1, right = 22
  Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
  Note:
  The boundaries of each input argument are 1 <= left <= right <= 10000.
  
  思路：对于小于10的，显然1-9；其他只要判断即可。
  
  """
def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if right < 10:
            return list(range(left, right+1))
        ans = []
        if left < 10:
            ans = list(range(left, 10))
            left = 10
        for i in range(left, right+1):
            num = i
          # 含0的直接跳过
            if '0' in str(num): continue
            while i % (num%10) == 0:
                num //= 10
              # 全部整除
                if num == 0:
                    ans.append(i)
                    break
        return ans

       
"""

"""
