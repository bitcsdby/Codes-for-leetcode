class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        map<int,int> record;
        map<int,int>::iterator ir;
        
        vector<int> vret;
        
        for(int i = 0;i < numbers.size();i++)
        {
            ir = record.find(target - numbers[i]);
            if(ir != record.end())
            {
                vret.push_back(ir->second+1);
                vret.push_back(i+1);
                return vret;
            }
            else
            {
                record[numbers[i]] = i;
            }
        }
        
        return vret;
    }
};