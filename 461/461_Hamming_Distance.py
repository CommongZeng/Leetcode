class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return '{:b}'.format(x^y).count('1')

test = Solution()
print test.hammingDistance(1, 4) # 2