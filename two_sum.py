# # Brute Force
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         length = len(nums)
#         for i in range(length):
#             for j in range(i+1,length):
#                 if nums[i] + nums[j] == target:
#                     return ([i,j])

# obj = Solution()
# print(obj.twoSum([23,4,5,7,3],8))

# # Hashmap with 2 loops
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         mapping = {}
#         for index,val in enumerate(nums):
#             mapping[val] = index

#         for i in range(len(nums)):
#             remaining = target-nums[i]
#             if remaining in mapping and mapping[remaining] != i:
#                 print(nums[i],remaining)
#                 return([i,mapping[remaining]])

# obj = Solution()
# print(obj.twoSum([23,4,5,7,3],28))	

# Hashmap with 1 loop O(n) memory and time complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for index, value in enumerate(nums):

            remaining = target - value
            if remaining in mapping:
                return [index, mapping[remaining]]
            else:
                mapping[value] = index

# obj = Solution()
# print(obj.twoSum([23,4,5,7,3],28))	


