class Solution {
public:
    bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false; // If they're not the same length, they can't be anagrams

    int counts[26] = {0}; // Initialize array to track character counts (yes, not a hash table; both work, but this is lighter and gives us the trick of using one loop with "- 'a'")
    for (int i = 0; i < s.size(); ++i) { // Using one loop like this is a nifty shortcut
        counts[s[i] - 'a']++; // Increment count for whatever character s[i] lands on; doing "- 'a'" is a nice trick, letting us refer to an array position 0-25 instead of a character 'a'-'z' as we'd have to in a hash table
        counts[t[i] - 'a']--; // Decrement count for whatever character t[i] lands on
    }

    for (int i = 0; i < 26; ++i) {
        if (counts[i] > 0) return false; // If a count is greater than zero, it means there was leftover characters, meaning NOT an anagram
    }
    return true; // All counts are zero, meaning there are the same number each character in both strings, meaning IS an anagram
    }
};
