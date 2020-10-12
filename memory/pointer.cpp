#include <iostream>

using namespace std;


struct Node {
    int value;
    Node *next;

    Node(int v, Node *n){
        value = v;
        next = n;
    }

};

void print_recursively(Node *node){
    if (node == NULL){
        cout << "NULL\n"; 
        return;
    }

    cout << node->value << "\n";
    print_recursively(node->next);
}

void print_reversed_recursively(Node *node){
    if (node == NULL){
        cout << "NULL\n";
        return;
    }

    print_reversed_recursively(node->next);
    cout << node->value << "\n";
}


int main()
{
    Node *head = new Node(1, NULL);
    head->next = new Node(2, NULL);

    print_recursively(head);
    print_reversed_recursively(head);

    return 0;
}
