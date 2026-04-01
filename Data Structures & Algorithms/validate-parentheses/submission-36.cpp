class Solution {
public:
    bool isValid(string s) {
        /*
        stack
        parens map
        
        */
        stack<char> bracketStack;
        unordered_map<char, char> bracketMap = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        for (const auto& c : s) {
            if (bracketMap.find(c) != bracketMap.end()){    
                if (!bracketStack.empty() && bracketMap[c] == bracketStack.top()){
                    bracketStack.pop();
                } else {
                    return false;
                }
            } else{
                bracketStack.push(c);
            }
        }
        return bracketStack.empty();
    }
};


