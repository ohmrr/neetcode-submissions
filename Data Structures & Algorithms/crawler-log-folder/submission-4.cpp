class Solution {
public:
    int minOperations(vector<string>& logs) {
        std::stack<string> stack;

        for (const std::string log : logs) {
            if (log == "../") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (log != "./") {
                stack.push(log);
            }
        }

        return stack.size();
    }
};