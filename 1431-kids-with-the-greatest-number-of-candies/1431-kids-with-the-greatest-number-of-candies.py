class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = 0
        for c in candies:
            if c > max_candies:
                max_candies = c
        result = []
        for c in candies:
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
