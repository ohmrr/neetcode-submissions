class Solution {
public:
    string removeVowels(string s) {
        std::unordered_set<char> vowels = { 'a', 'e', 'i', 'o', 'u' };
        std::vector<char> new_chars;

        for (char ch : s) {
            if (vowels.contains(ch)) {
                continue;
            }

            new_chars.push_back(ch);
        }

        std::string str(new_chars.data(), new_chars.size());
        return str;
    }
};
