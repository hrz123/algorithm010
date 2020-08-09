//
// Created by Ruizhe Hou on 2020/6/17.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 // 递归的方法
 class Solution{
 public:
     vector<int> inorderTraversal(TreeNode* root) {
         vector<int> nodes;
         inorder()
     }
 };

// 迭代的方法，使用栈
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> nodes;
        stack <TreeNode*> st;
        while (root || !st.empty()) {
            while (root) {
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            nodes.push_back(root->val);
            root = root->right;
        }
        return nodes;
    }
};
