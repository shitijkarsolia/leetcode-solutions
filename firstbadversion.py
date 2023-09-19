# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 5:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0 
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid) == True:
                right = mid - 1
            else:
                left = mid + 1                
        return right

obj = Solution()
n = 7
print(obj.firstBadVersion(n))