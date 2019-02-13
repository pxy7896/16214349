"""
Reverse bits of a given 32 bits unsigned integer.
Input: 43261596
Output: 964176192
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.

python提供bin函数直接转为二进制字符串，不过前两位是0b，要去掉。直接翻转，补全32位，再int转为整数即可。

"""
def reverseBits(self, n):
        bins = bin(n)[2:][::-1]
        ans = bins + '0'*(32-len(bins))
        return int(ans, 2)

