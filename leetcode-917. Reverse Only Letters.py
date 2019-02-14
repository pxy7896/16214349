"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
and all letters reverse their positions.
Example :
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

题意是只翻转[a,z][A,Z]，其他字符保持不动。所以单层循环，俩指针即可。

"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) < 2: return S
        if S.isalpha(): return S[::-1]
        first = 0
        last = len(S) - 1
        ans = list(S)
        while first < last:
            if ans[first].isalpha() == False:
                first += 1
            elif ans[last].isalpha() == False:
                last -= 1
            else:
                ans[first], ans[last] = ans[last], ans[first]
                first += 1
                last -= 1
        return "".join(ans)

