'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenght = len(s)
        aws = 0
        for i in range(lenght):
            for j in range(i + 1, lenght):
                if self.allUnique(s, i, j):
                    aws = aws if aws > j - i else j - i
        print(aws)
        return aws

    def allUnique(self, s, start, end):
        set_ = set()
        for i in range(start, end):
            print(set_)
            if s[i] in set_:
                return False
            else:
                set_.add(s[i])

        return True


solution = Solution()

assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3

# Time complexility:

n(i+1)O(j-i)