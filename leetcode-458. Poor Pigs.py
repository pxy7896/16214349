"""
There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. 
If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out 
which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the 
"poison" bucket within p minutes? There is exact one bucket with poison.

"""

对于原始问题来说，我们只有4次测试机会，所以一头猪可以检查5个桶。当有两头猪时，可以一头检查行，一头检查列，所以可以检查25个桶。当有三头猪
时，可以变成一个5*5*5的立方体。因此，只要计算出可进行的test数目，然后再计算满足(test+1)^pig >= buckets时的pig即是答案。

需要注意的是，对于1,1,1的case，我认为应该返回1，然而WA了。leetcode希望我返回0 :）

def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest//minutesToDie+1) ** pigs < buckets:
            pigs += 1
        return pigs
