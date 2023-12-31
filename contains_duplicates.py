class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_mapping = set()
        for ele in nums:
            if ele in count_mapping:
                return True
            else:
                count_mapping.add(ele)
        return False

obj = Solution()
print(obj.containsDuplicate([1,5,-2,-4,1]))