
"""
#leetcode
#No.7 Reverse integrate
#暴力破解法 -> O(n)
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note: Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−2^31, 2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
            minus_flag = False
            i, x_len = 0, len(str(x))
            result = x
            temp = 0


            if x < 0:
                minus_flag = True
                result *= -1
                x_len -= 1

            for i in range(x_len):
                temp = result%10 + temp*10
                result = result//10
                print(result,"-",i)
            if minus_flag:
                temp *= -1

            if temp < -2**31 or temp > 2**31-1:
                return 0
                
            return temp

mm = Solution()
result = mm.reverse(123)
print(result)