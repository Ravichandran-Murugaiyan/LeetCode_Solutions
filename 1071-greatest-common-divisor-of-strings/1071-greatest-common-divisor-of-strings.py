class Solution:
    def gcdOfStrings(self, str1,str2):
        if str1 + str2 != str2 + str1:
            return ""
        
        def find_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        gcd_length = find_gcd(len(str1), len(str2))
        
        return str1[:gcd_length]
