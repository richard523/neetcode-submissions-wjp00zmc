class MinStack {
private:
    std::stack<int> stack;
    std::stack<int> minStack; // why
public:
    MinStack() {}
    
    void push(int val) {
        stack.push(val);
        val = std::min(val, minStack.empty() ? val : minStack.top()); // what and why
        minStack.push(val); // why
    }
    
    void pop() {
        stack.pop();
        minStack.pop(); // why
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
