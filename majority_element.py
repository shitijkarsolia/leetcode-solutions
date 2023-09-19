class Solution():
    # Time Complexity: O(n)
    # Memory Complexity: O(n)
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # [1,1,1,2,2,2,2]
    #     majority_element = 0
    #     count_map = {}
    #     max_count = 0
    #     for element in nums:
    #         if element in count_map:
    #             count_map[element] = count_map[element] + 1
    #         else:
    #             count_map[element] = 1

    #         if count_map[element] > max_count:
    #             max_count = count_map[element]
    #             majority_element = element
    #     if max_count > len(nums)/2:
    #         return majority_element
    #     return "Invalid Input"

# Using Boyer-Moore's Voting algorithm
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,1,1,2,2,2,2]
        majority_element = nums[0]
        count = 0 
        for element in nums:
            if element == majority_element:
                count = count + 1
            else:
                if count == 0:
                    majority_element = element
                    count = count + 1
                else:
                    count = count - 1

        check = 0
        for ele in nums:
            if ele == majority_element:
                check +=1
        
        if check > len(nums)//2:
            return majority_element
        else:
            return "Invalid Input"


obj = Solution()
print(obj.majorityElement([1,1,1,2,2,2,1]))