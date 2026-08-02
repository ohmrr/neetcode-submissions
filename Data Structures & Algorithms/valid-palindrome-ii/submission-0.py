class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
                continue

            left_removed = s[left + 1:right + 1]
            right_removed = s[left:right]
            
            if left_removed == left_removed[::-1]: return True
            elif right_removed == right_removed[::-1]: return True
            else: return False

        return True