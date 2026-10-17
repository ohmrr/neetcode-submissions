class Solution {
public:
    int sumOfDigits(vector<int>& nums) {
        int minimum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < minimum) {
                minimum = nums[i];
            }
        }

        int sum = 0;
        while (minimum > 0) {
            sum += minimum % 10;
            minimum /= 10;
        }

        return sum % 2 == 0 ? 1 : 0;
    }
};
