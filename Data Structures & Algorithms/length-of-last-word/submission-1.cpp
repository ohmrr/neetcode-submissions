class Solution {
public:
    int lengthOfLastWord(string s) {
        int start = s.size() - 1;
        int length = 0;

        while ((!isalnum(s[start])) || (isalnum(s[start]) && isalnum(s[start - 1]))) {
            start--;
        }

        for (int i = start; i < s.size(); i++) {
            if (!isalnum(s[i])) {
                break;
            }

            length++;
        }

        return length;
    }
};