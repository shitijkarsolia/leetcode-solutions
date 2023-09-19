class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_magazine = {}
        for letter in magazine:
            count_magazine[letter] = count_magazine.get(letter,0) + 1
        
        for l in ransomNote:
            if count_magazine.get(l,0):
                count_magazine[l] = count_magazine[l] - 1
            else:
                return False
        
        return True


obj = Solution()
s = "rab"
t = "abcdefp"

print(obj.canConstruct(s,t))