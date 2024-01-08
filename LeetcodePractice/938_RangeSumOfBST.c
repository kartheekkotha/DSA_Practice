// Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int rangeSumBST(struct TreeNode* root, int low, int high) {
    int sum = 0;
    helper(root , low , high , &sum);
    return sum;
}

void helper(struct TreeNode * root , int low , int high , int * sum){
    if(root == NULL){
        return ;
    }
    helper(root->left , low , high , sum);
    if(root->val >=low && root->val <=high){
        *sum = (*sum) + root->val;
    }
    helper(root->right , low , high , sum);
}