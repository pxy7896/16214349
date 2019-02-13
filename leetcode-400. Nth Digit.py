"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Example 2:
Input:
11
Output:
0
Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

首先确定有几位数字，然后重建数，挑出数字

"""

def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = 1
        num = n
        while num > 0:
            pre = num
            num -= w * 9 * 10 ** (w-1)
            w += 1
        # reconstruct number
        ans = 10**(w-2) + (pre-1)//(w-1)
        # find digit
        return int(str(ans)[(pre-1)%(w-1)])
