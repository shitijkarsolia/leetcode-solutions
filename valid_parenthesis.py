"""
pseudocode
create a mapping of opening:closing
iterate over string 
if bracket is opening push to stack
if bracket is closing, pop from stack and compare if the mapped closing bracket for the stack open bracket is the same or not
return true/false

"""
class Solution(object):
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
        "{":"}",
        "[":"]",
        "(":")"
        }
        for bracket in s:
            # if opening bracket
            if bracket in mapping:
                stack.append(bracket)
            # if closing bracket, compare with stack's closing bracket
            else:
                if len(stack) ==0 :
                    return False
                closing = mapping[stack.pop()]
                if closing != bracket:
                    return False
        if len(stack):
            return False
        
        return True
            
obj = Solution()
s = "[[{()}]]"
print(obj.isValid(s))
