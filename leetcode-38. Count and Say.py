"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

基于前一个产生下一个，直接递归做即可。

"""
def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        s = self.countAndSay(n - 1)
        ans = []
        cnt = 1
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                # 直接读取，计数
                ans += [str(cnt), s[i]]
                cnt = 1
            else:
                cnt += 1
        return ''.join(ans)
        
