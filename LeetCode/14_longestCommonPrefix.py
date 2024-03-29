"""
#leetcode
#No.14 longestCommonPrefix
#string 地址查找对比 -> O(n**2)
"""

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_str = ""
        minum_len = len(min(strs, key=len, default=""))
        left_point = 0

        for i in range(minum_len):
            
            for current_str in strs:
                if longest_str == current_str[left_point : i+1]:
                    continue
                else:
                    left_point = i + 1
                    break
