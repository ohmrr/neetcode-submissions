class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int i = n - 1;

        while (isspace(s[i])) {
            i--;
        }

        int length = 0;
        while (i >= 0 && isalnum(s[i])) {
            length++;
            i--;
        }

        return length;
    }
};