class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> result(temperatures.size(), 0);
        std::stack<std::pair<int, int>> stack; // (index, temperature)

        for (int i = 0; i < temperatures.size(); i++) {
            while (!stack.empty() && stack.top().second < temperatures[i]) {
                auto pair = stack.top();
                stack.pop();

                result.at(pair.first) = i - pair.first;
            }

            stack.push({ i, temperatures[i] });
        }

        return result;
    }
};
