#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node* prev;

    Node(int val){
        this->data= val;
        this->next=NULL;
        this->prev=NULL;
    }
    ~Node(){
        if(next!=NULL && prev!=NULL){
            delete(next);
            delete(prev);
            this->prev=NULL;
            this->next=NULL;
        }
        
    }
};

void insertAtHead(Node*&head, int val,Node*&tail){
    Node* temp= new Node(val);
    if(head==NULL){
        head=temp;
        return;
    }
    temp->prev=tail;
    head->next=temp;
    temp->next=head;
    head->prev=temp;
    head=temp;
}

void insertAtTail(Node*&tail, int val,Node*&head){
    Node* temp= new Node(val);
    tail->next=temp;
    temp->prev=tail;
    temp->next=head;
    head->prev=temp;
    tail=temp;
}

void insertAtMiddle(Node*&head, int val, int pos){
    Node*temp=head;
    while(pos>1){
        temp=temp->next;
        pos--;
    }
    Node* newNode= new Node(val);
    newNode->next=temp->next;
    temp->next=newNode;
    newNode->prev=temp;
}

void deleteNode(Node*&head, int val){
    Node*temp=head;
    Node* pre=NULL;
    if(temp->data==val){
        head=temp->next;
        temp->next=NULL;
        head->prev=NULL;
        delete temp;
        return;
    }
    
    while(temp->data!=val){
        pre=temp;
        temp=temp->next;
    }
    pre->next=temp->next;
    pre->next->prev=pre;
    temp->next=NULL;
    temp->prev=NULL;
    delete temp;
}

void print(Node* head){
    Node* temp=head;
    do{
        cout<<temp->data<<" ";
        temp=temp->next;
    }while(temp!=head);
    cout<<endl;
}
int main(){
    Node* head= new Node(10);
    Node* tail=head;
    insertAtHead(head, 20,tail);
    insertAtTail(tail,30,head);
    insertAtMiddle(head,25,2);
    print(head);
    deleteNode(head, 25 );
    print(head);
    return 0;
}