class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # {} To store unique characters in the current window
        left = 0  # Start of the window
        max_length = 0

        for right in range(len(s)):  # Expand the window with the right pointer
            while s[right] in char_set:  # Shrink the window if a duplicate is found
                char_set.remove(s[left])
                left += 1  # Move the left pointer to the right

            char_set.add(s[right])  # Add the current character to the window
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length


Input = "pwwkew"
sol = Solution()
sol.lengthOfLongestSubstring(Input)
print(sol.lengthOfLongestSubstring(Input))

