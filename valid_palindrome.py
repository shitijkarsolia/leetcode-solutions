class Solution(object):

    def alphaNum(self,character):
        if (ord('A') <= ord(character) <= ord('Z') or
            ord('a') <= ord(character) <= ord('z') or
            ord('0') <= ord(character) <= ord('9')):
            return True
        else:
            return False


    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1
        while right > left:

            # Compare only lowercase and alphanumeric characters
            if not self.alphaNum(s[left]):
                left += 1
                continue

            if not self.alphaNum(s[right]):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True


obj = Solution()
s = "A man, a plan, a canal: Panama"
response = obj.isPalindrome(s)
print(response)

print(s.lower())