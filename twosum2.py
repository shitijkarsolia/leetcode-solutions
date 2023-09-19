class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_ptr = 0
        right_ptr = len(numbers)-1
        for i in range(0,len(numbers)):
            # print([left_ptr,right_ptr])
            sum = numbers[left_ptr] + numbers[right_ptr]
            if left_ptr == right_ptr:
                return "No Solution for given input!"
            if sum > target:
                right_ptr -=1
            elif sum < target:
                left_ptr +=1
            elif sum == target:
                return [left_ptr+1,right_ptr+1]
            else:
                return "No Solution for given input!"

obj = Solution()
numbers = [2,5,7,8,10]
target = 16
print(obj.twoSum(numbers,target))