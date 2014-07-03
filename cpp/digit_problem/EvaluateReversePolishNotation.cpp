class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int> num;
        
        for(int i = 0;i < tokens.size();i++)
        {
            if(tokens[i] == "+")
            {
                int num1 = num.top();
                num.pop();
                int num2 = num.top();
                num.pop();
                
                num.push(num1 + num2);
            }
            else if(tokens[i] == "-")
            {
                int post = num.top();
                num.pop();
                int pre = num.top();
                num.pop();
                
                num.push(pre - post);
                
            }
            else if(tokens[i] == "*")
            {
                int num1 = num.top();
                num.pop();
                int num2 = num.top();
                num.pop();
                
                num.push(num1 * num2);
                
            }
            else if(tokens[i] == "/")
            {
                int post = num.top();
                num.pop();
                int pre = num.top();
                num.pop();
                
                num.push(pre / post);
            }
            else
            {
                num.push(atoi(tokens[i].c_str()));
            }
        }
        
        return num.top();
    }
};