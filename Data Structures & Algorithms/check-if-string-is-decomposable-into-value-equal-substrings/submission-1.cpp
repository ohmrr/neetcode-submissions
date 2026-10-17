class Solution {
public:
    bool isDecomposable(string s) {
        int n = s.size();
        int numPairs = 0;

        int i = 0;
        while (i < n) {
            int j = i;

            while (j < n && s[i] == s[j]) {
                j++;
            }

            std::cout << j << std::endl;

            if ((j - i) % 3 == 1) {
                return false;
            } else if ((j - i) % 3 == 2) {
                numPairs++;
            }

            i = j;
        }

        return numPairs == 1;
    }
};
