#include<iostream>
#include<queue>
using namespace std;

struct node {
    int data;
    node* left;
    node* right;

    node(int data){
        this->data=data;
        this->left=NULL;
        this->right=NULL;
    }
};

// node* buildTree(node* root){
//     cout<<"Enter data: ";
//     int data;
//     cin>> data;
//     if(data==-1){
//         return NULL;
//     }
//     cout<<"Enter left child of "<<data<<" : ";
//     root->left=buildTree(root->left);
//     cout<<"Enter right child of "<<data<< " : ";
//     root->right=buildTree(root->right);
//     return root;
    
// }

node* buildTree(){
    cout << "Enter data: ";
    int data;
    cin >> data;

    // Base case: if the data is -1, return NULL (no node)
    if (data == -1) {
        return NULL;
    }

    // Create a new node with the given data
    node* newNode = new node(data);

    // Recursively build the left and right subtrees
    cout << "Enter left child of " << data << " : ";
    newNode->left = buildTree();
    cout << "Enter right child of " << data << " : ";
    newNode->right = buildTree();
    
    return newNode;
}

void levelOrderTraversal(node* root){
    cout<<endl;
    queue<node*> q;
    q.push(root);
    q.push(NULL);
    while(!q.empty()){
        node* temp= q.front();
        q.pop();
        if(temp==NULL){
            cout<<endl;
            if(!q.empty()){
                q.push(NULL);
            }
            continue;
        }
        cout<<temp->data<<" ";
        if(temp->left){
            q.push(temp->left);
        }
        
        if(temp->right){
            q.push(temp->right);
        }
    }
}

void PreOrderTraversal(node*root){
    if(root==NULL){
        return;
    }
    cout<<root->data<<" ";
    PreOrderTraversal(root->left);
    PreOrderTraversal(root->right);
}

node* buildLevelTree(){
    node* newNode;
    int data;
    cin>>data;
    newNode = new node(data);

    queue<node*> q;
    q.push(newNode);
    while(!q.empty()){
        node* temp= q.front();
        q.pop();
        cout<<"Enter left child of "<<temp->data<<" : ";
        cin>>data;
        if(data!=-1){
            temp->left= new node(data);
            q.push(temp->left);
        }
        cout<<"Enter right child of "<<temp->data<<" : ";
        cin>>data;
        if(data!=-1){
            temp->right= new node(data);
            q.push(temp->right);
        }
    }
    return newNode;
}

int main(){
    // 7 4 2 -1 -1 2 -1 -1 3 -1 -1
    // node* root = buildTree();
    // node* root = buildLevelTree(); 
    // levelOrderTraversal(root);
    PreOrderTraversal(root);
    return 0;
}