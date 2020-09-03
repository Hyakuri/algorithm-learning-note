
"""
#leetcode
#No.7 Reverse integrate
#string双向指针 -> O(n)
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
        str_x = str(x)
        x_len = len(str_x)
        right_point = x_len - 1 
        left_point = 0
        if x < 0:
            left_point += 1

        str_x = list(str_x)
        # print(right_point)
        # print(str_x)
        while(right_point > left_point):
            temp_char = str_x[left_point]
            str_x[left_point] = str_x[right_point]
            str_x[right_point] = temp_char
            right_point -= 1
            left_point +=1

        result = int("".join(str_x))
        if result < -(1<<31) or result > (1<<31) -1:
            return 0
        else:
            return result



mm = Solution()
result = mm.reverse(2<<31)
print(result)