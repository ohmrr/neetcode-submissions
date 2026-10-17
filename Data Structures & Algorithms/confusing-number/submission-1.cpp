class Solution {
public:
    bool confusingNumber(int n) {
        std::unordered_map<char, char> rotated_map = {
            { '0', '0' },
            { '1', '1' },
            { '6', '9' },
            { '8', '8' },
            { '9', '6' }
        };
        auto numStr = std::to_string(n);
        std::string rotated;

        for (int i = numStr.size() - 1; i >= 0; i--) {
            if (!rotated_map.contains(numStr[i])) return false;

            rotated += rotated_map[numStr[i]];
        }

        return rotated != numStr;
    }
};
