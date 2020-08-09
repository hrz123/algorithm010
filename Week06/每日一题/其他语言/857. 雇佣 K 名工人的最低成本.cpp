//
// Created by Ruizhe Hou on 2020/7/13.
//
#include <vector>
#include <utility>
#include <queue>

using namespace std;

class Solution {
public:
    double mincostToHireWorkers(vector<int> &quality, vector<int> &wage, int K) {
        int n = quality.size();
        vector<pair<double, double>> v(n);
        for (int i = 0; i < n; ++i) {
            v[i] = {quality[i], wage[i]};  //pair literal
        }
        sort(begin(v), end(v), [&](auto v1, auto v2) {
            return v1.second / v1.first < v2.second / v2.first;
        });
        priority_queue<double> pq;
        double ans = 1e35, sum = 0;
        for (auto &&[q, w]: v) {  // 直接&[x, y]可以展开pair
            sum += q;
            pq.push(q);
            if (pq.size() > K) {
                sum -= pq.top();
                pq.pop();
            }
            if (pq.size() == K) {
                ans = min(ans, sum * w / q);
            }
        }
        return ans;
    }
};

