#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstring>

using namespace std;

template <class Type>
class TreeNode {
  public:
  Type data;
  TreeNode(Type dataIn) {
    data = dataIn;
  }
  TreeNode* left = NULL;
  TreeNode* right = NULL;
};

template <class Type>
class BinaryTree {
  public:
  TreeNode<Type>* root;
  BinaryTree(Type inData) {
    root = new TreeNode<Type>(inData);
  }
  BinaryTree<Type> add(Type data){
    if (root == NULL) {
      root = new TreeNode<Type>(data);
      return 0;
    } else {
      TreeNode<Type>* curNode = root;
      while (true) {
        if (curNode->data >= data) {
          if (curNode->left == NULL) {
            curNode->left = new TreeNode<Type>(data);
             return *this;
          } else {
            curNode = curNode->left;
          }
        } else {
          if (curNode->right == NULL) {
            curNode->right = new TreeNode<Type>(data);
             return *this;
          } else {
            curNode = curNode->right;
          }
        }
      }
    }
    // return this;
  }
  int* inOrderTravers(Type E) {
    int maxLength = -1;
    int maxDepth = 0;
    int curDepth = 0;
    if (root != NULL) {
      if (root->left != NULL) {
        inOrderTravers(root->left, E, maxLength, maxDepth, curDepth);
      }
      if (root->data == E) {
        maxLength = max(0, maxLength);
      }
      if (root->right != NULL) {
        inOrderTravers(root->right, E, maxLength, maxDepth, curDepth);
      }
      cout << "Максимальная глубина узла " << E << " равна " << maxLength << endl;
      cout << "Максимальная глубина равна " << maxDepth << endl;
      static int res[2] = {maxLength, maxDepth};
      return res;
    }
  }
  int inOrderTravers(TreeNode<Type>* node, Type E, int &maxLength, int &maxDepth, int &curDepth) {
    curDepth += 1;
    if (node->left != NULL) {
      inOrderTravers(node->left, E, maxLength, maxDepth, curDepth);
    }
    if (node->data == E) {
      maxLength = max(curDepth, maxLength);
    }
    maxDepth = max(maxDepth, curDepth);
    if (node->right != NULL) {
      inOrderTravers(node->right, E, maxLength, maxDepth, curDepth);
    }
    curDepth -= 1;
  }
};


int main() {
  BinaryTree<int> s(32);
  // s.add(25).add(45).add(32).add(33);
  // s.inOrderTravers(32);
  // string str = "0";
  // while (true){
  //   getline(cin, str);
  //   // cin >> str;
  //   cout << "S:" << str << ":F" << "\n";
  //   if (str == "end") {
  //     cout << "максимальная глубина для ";
  //     int vertex;
  //     cin >> vertex;
  //     s.inOrderTravers(vertex);
  //     break;
  //   }    
  // }
  string str = "0";
  while (getline(cin, str)){
    if ((str == "end")) {
      cout << "максимальная глубина для ";
      int vertex;
      cin >> vertex;
      s.inOrderTravers(vertex);
      break;
    }   
    s.add(atoi(str.c_str())); 
  }
  return 0;
}