"""
Your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

由于headers和houses可能是乱序，所以要先排序。然后给heaters两端各加一个假的heater，这样所有house都会在heater之中。对每一个house，检查它与两端
heaters的距离，较小的那个辐射半径就足够了，然后找出这些辐射半径里的最大值，保证所有房子都可以辐射的到。

"""

def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        ans, i = 0, 0
        new_heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house > new_heaters[i + 1]:
                i += 1
            min_dis = min(house-new_heaters[i], new_heaters[i+1]-house)
            ans = max(ans, min_dis)
        return ans
