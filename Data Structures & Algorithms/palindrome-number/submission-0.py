class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_num = str(x)
        return str_num == str_num[::-1]