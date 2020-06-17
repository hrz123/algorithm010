//
// Created by Ruizhe Hou on 2020/6/17.
//

class Solution {
public:
    int maxScoreSightseeingPair(vector<int> &A) {
        int ans = 0, mx = A[0] + 0;
        int size = A.size();
        for (int j = 1; j < A.size(); ++j) {
            ans = max(ans, mx + A[j] - j);

            mx = max(mx, A[j] + j);
        }
        return ans;
    }
};
