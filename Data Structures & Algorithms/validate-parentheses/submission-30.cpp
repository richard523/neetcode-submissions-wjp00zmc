class Solution {
public:
    bool isValid(string s) {
        stack<char> open;
        unordered_map<char, char> parens = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        for (const auto& c : s) {
            if (parens.find(c) != parens.end()) { // if we DO have result from .find()
                if (!open.empty() && open.top() == parens[c]){
                    open.pop();
                }
                else {
                    return false;
                }
            } else {
                open.push(c);
            }
        }
        
        return open.empty();
    }
};


