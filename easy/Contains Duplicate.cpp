class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> count; // hash table for keping count; key for number, value for count of number appearances
        for (int i = 0; i < nums.size(); ++i) {
            if (++count[nums[i]] >= 2) // increment counts and check for target case in one line
                return true; // if target case is true, return true
        }
        return false; // no target case found
    }
};
