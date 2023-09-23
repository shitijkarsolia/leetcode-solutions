class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        answer = ""
        max_len = max(len(a),len(b))
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:   
            a_val = int(a[i]) if i>=0 else 0
            i = i - 1
            b_val = int(b[j]) if j>=0 else 0
            j = j - 1

            sum = a_val + b_val + carry
            carry = sum // 2
            digit = sum % 2
            answer = str(digit) + answer
        return answer
obj = Solution()
a= "11"
b="1"
print(obj.addBinary(a,b))