class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> output;

        int prefix = 1;
        for (int i = 0; i < nums.size(); i++) {
            output.push_back(prefix);
            prefix *= nums.at(i);
        }

        int postfix = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            output.at(i) *= postfix;
            postfix *= nums.at(i);
        }

        return output;
    }
};
