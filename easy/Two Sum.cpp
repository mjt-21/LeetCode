class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numsHash; // hash table where key is number, value is vector index of that number
        
        for (int i = 0; i < nums.size(); ++i) {
            if (numsHash.find(target - nums[i]) == numsHash.end()) // if number that added to the current number is not found in hash table
                numsHash[nums[i]] = i; // add current number and its index to hash table
            else
                return {numsHash[target - nums[i]], i}; // found needed value, return both indexes
        }
        
        return {};
    }
};
