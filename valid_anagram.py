class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_character_count = {}
        t_character_count = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_character_count[s[i]] = s_character_count.get(s[i],0) + 1
            t_character_count[t[i]] = t_character_count.get(t[i],0) + 1

        for letter in s_character_count:
            if s_character_count[letter] != t_character_count.get(letter,0):
                return False
        return True

        # return sorted(s) == sorted(t)

obj = Solution()
s = "anagram"
t = "gramsaa"

print(obj.isAnagram(s,t))
