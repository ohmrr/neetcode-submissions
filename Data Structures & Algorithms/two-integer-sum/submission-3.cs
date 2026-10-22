public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Key : Value ==> Value : Index
        var dict = new Dictionary<int, int>();

        for (var i = 0; i < nums.Length; i++) {
            var difference = target - nums[i];

            if (dict.ContainsKey(difference)) {
                return [dict[difference], i];
            }

            dict.Add(nums[i], i);
        }

        return [-1, -1];
    }
}
