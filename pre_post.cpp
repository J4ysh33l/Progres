#include <iostream>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BinaryTree {
public:
    // Function for pre-order traversal
    void preorderTraversal(TreeNode* root) {
        if (root == nullptr) return;
        cout << root->val << " "; // Process the current node
        preorderTraversal(root->left); // Recur on the left subtree
        preorderTraversal(root->right); // Recur on the right subtree
    }

    // Function for post-order traversal
    void postorderTraversal(TreeNode* root) {
        if (root == nullptr) return;
        postorderTraversal(root->left); // Recur on the left subtree
        postorderTraversal(root->right); // Recur on the right subtree
        cout << root->val << " "; // Process the current node
    }
};

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    BinaryTree bt;

    cout << "Pre-order traversal: ";
    bt.preorderTraversal(root);
    cout << endl;

    cout << "Post-order traversal: ";
    bt.postorderTraversal(root);
    cout << endl;

    // Clean up memory
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}


 
