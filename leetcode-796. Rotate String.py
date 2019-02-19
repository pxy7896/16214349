'''
Return True if and only if A can become B after some number of shifts on A.
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

思路：本来想两个指针遍历比较一下，结果发现case里有"bbbacddceeb"和"ceebbbbacdd"（显然要判断为True，但是index只返回第一次找到的位置，所以遍历的方法
会返回False）。所以直接把A*2就好了，只要B在里面即可。

'''
def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if len(A) < 2: return A==B
        if set(A) != set(B): return False
        return B in A*2
        # 下面这些就是瞎扯淡：）
        '''
        size = len(A)
        j = B.index(A[0])
        
        for i in range(size):
            if j == size:
                j = 0
            
            if A[i] == B[j]:
                j += 1
            else:
                break
        else:
            return True
        return False
        '''
        
