class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> closedToOpen = {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };
        std::stack<char> stack;

        for (int i = 0; i < s.size(); i++) {
            if (closedToOpen.contains(s[i])) {
                // if a closing bracket
                if (stack.size() > 0 && closedToOpen[s[i]] == stack.top()) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                // if an opening bracket
                stack.push(s[i]);
            }
        }

        return stack.size() == 0;
    }
};
