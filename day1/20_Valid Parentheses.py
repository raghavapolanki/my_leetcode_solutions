Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

expl
----
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                # Invalid character
                return False

        # The string is valid if the stack is empty at the end
        return not stack

s = Solution()

# Example usage:
example1 = "()"
result1 = s.isValid(example1)
print(result1)  # Output: True

example2 = "()[]{}"
result2 = s.isValid(example2)
print(result2)  # Output: True

example3 = "(]"
result3 = s.isValid(example3)
print(result3)  # Output: False
