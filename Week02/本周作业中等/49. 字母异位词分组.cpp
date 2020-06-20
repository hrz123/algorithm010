// 解法1：使用内置的排序函数
class Solution {
public:
    vector <vector<string>> groupAnagrams(vector <string> &strs) {
        unordered_map <string, vector<string>> mp;
        for (string s : strs) {
            string t = s;
            sort(t.begin(), t.end());
            mp[t].push_back(s);
        }
        vector <vector<string>> anagrams;
        for (auto p:mp) {
            anagrams.push_back(p.second);
        }
        return anagrams;
    }
};

// 解法2：使用计数排序
class Solution {
public:
    vector <vector<string>> groupAnagrams(vector <string> &strs) {
        unordered_map <string, vector<string>> mp;
        for (string s : strs) {
            mp[strSort(s)].push_back(s);
        }
        vector <vector<string>> anagrams;
        for (auto p : mp) {
            anagrams.push_back(p.second);
        }
        return anagrams;
    }

private:
    string strSort(string s) {
        int counter[26] = {0};
        for (char c : s) {
            counter[c - 'a']++;
        }
        string t;
        for (int c = 0; c < 26; c++) {
            t += string(counter[c], c + 'a');
        }
        return t;
    }
};