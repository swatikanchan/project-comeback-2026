## Problems solved

    1. Valid Palindrome
        Data structure used: variables
        Time complexity: O(n), where n is the length of the string
        Space complexity: O(1)
        One sentence describing the key insight

    2. Merge Two Sorted Lists
        Data structure used: Variables
        Time complexity: O(m+n), where m and n are length of the linput ists
        Space complexity: O(1)
        One sentence describing the key insight

    3. Binary Search
        Data structure used: variables
        Time complexity: O(log n), where n is the length of input array
        Space complexity: O(1)
        One sentence describing the key insight

## Debugging Log

    Problem:
    ModuleNotFoundError: No module named 'calculator'

    Root Cause:
    Ran unittest from project root while using a local module import.

    Solution:
    Run tests from the package directory (for now) and later adopt a proper package structure.