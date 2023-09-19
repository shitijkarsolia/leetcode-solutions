class Solution():
    def search(self, nums, target):
        """
        """
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1

obj = Solution()
nums = [-4,4,5,6,7,8,88]
target = 77
response = obj.search(nums,target)
print(response)
