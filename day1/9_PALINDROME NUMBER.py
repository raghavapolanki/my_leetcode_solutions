Given an integer x, return true if x is a  palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special case: Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Reverse the second half of the number and compare it with the first half
        reversed_half = 0
        original_x = x
        
        while x > 0:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        return original_x == reversed_half


s = Solution()

# Example 1: Palindrome
x1 = 121
print(s.isPalindrome(x1))  # Output: True

# Example 2: Not a palindrome (negative number)
x2 = -121
print(s.isPalindrome(x2))  # Output: False

# Example 3: Not a palindrome (ends with 0)
x3 = 10
print(s.isPalindrome(x3))  # Output: False

# Example 4: Palindrome
x4 = 1221
print(s.isPalindrome(x4))  # Output: True

# Example 5: Not a palindrome
x5 = 12345
print(s.isPalindrome(x5))  # Output: False


expl:
-----
Class Definition:

The code defines a class named Solution.
Method isPalindrome:

The class contains a method called isPalindrome.
It takes one parameter, x, an integer.
The return type is specified as a boolean (bool).
Special Case Handling (Negative Numbers):

The code begins by checking if the input number x is negative. If it is, negative numbers are not palindromes, so the method returns False.
Initialization:

The code initializes two variables:
reversed_half is used to store the reversed second half of the number.
original_x is a copy of the original number x. This is used for the final comparison.
Reversing the Second Half:

The code enters a while loop, which continues as long as x is greater than 0.
Inside the loop:
digit is calculated as the last digit of x using the modulo operator (x % 10).
The reversed_half is updated by multiplying it by 10 (shifting digits to the left) and adding the current digit.
The last digit is removed from x by performing integer division (x //= 10).
Comparison:

After the while loop, the code compares the original number original_x with the reversed second half (reversed_half).
If they are equal, the number is a palindrome, and the method returns True.
If they are not equal, the method returns False.
This algorithm efficiently checks if an integer is a palindrome without converting it to a string. The time complexity is O(log10(x)), where x is the input number, as we iterate through the digits of the number. The space complexity is O(1), as we use a constant amount of extra space.
