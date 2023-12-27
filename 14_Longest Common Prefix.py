Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


expl:
----

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the array of strings to simplify comparison
        strs.sort()

        # Take the first and last strings in the sorted array
        first_str, last_str = strs[0], strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return "".join(common_prefix)



s = Solution()

# Example usage:
strs1 = ["flower", "flow", "flight"]
result1 = s.longestCommonPrefix(strs1)
print(result1)  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
result2 = s.longestCommonPrefix(strs2)
print(result2)  # Output: ""




This function first sorts the array of strings to make it easier to compare the first and last strings. It then iterates through the characters of the first and last strings, stopping when a mismatch is found. The common prefix is constructed based on the matching characters. The time complexity of this function is O(m * n), where m is the length of the longest string and n is the number of strings in the array.