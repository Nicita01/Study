#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class node {
    public:
    double data;
    node* next;
    node(double dataIn) {
      next = NULL;
      data = dataIn;
    };
  };

class list {
    public:
    node* first;
    node* last;
  };

float* maxMin(list X);
float* makerY(list X, float coef, int strCount);
float* makerZ(float* Y, int strCount);
void output(float* Y, float* Z, int strCount);

int main() {
  ifstream fin;
  fin.open("MicroSoft.csv");
  string str;
  getline(fin, str);
  str = str.substr(str.find(',') + 1);
  str = str.substr(0, str.find(','));
  list X;
  X.first = new node(atof(str.c_str()));
  X.last = X.first;
  int strCount = 1;
  while (!fin.eof()) {
    string str = "";
    getline(fin, str);
    str = str.substr(str.find(',') + 1);
    if (str.size()) {
      strCount++;
      str = str.substr(0, str.find(','));
      X.last->next = new node(atof(str.c_str()));
      X.last = X.last->next;
    };
  }
  fin.close();
  float* maxMinArray = maxMin(X);
  float Y_max = 5587.65;
  float Y_min = 16.3516;
  float coef = (Y_max - Y_min) / (maxMinArray[1] - maxMinArray[0]);
  float* Y = makerY(X, coef, strCount);
  float* Z = makerZ(Y, strCount);
  output(Y, Z, strCount);
  delete[] Y;
  delete[] Z;
  return 0;
}

float* maxMin(list X) {
  float max = X.first->data;
  float min = X.first->data;
  node* curNode = X.first;
  while(curNode->next != NULL) {
    curNode = curNode->next;
    if (curNode->data > max) {
      max = curNode->data;
    }
    if (curNode->data < min) {
      min = curNode->data;
    }
  }
  static float res[2] = {min, max};
  return res;
}

float* makerY(list X, float coef, int strCount) {
  float* Y = new float[strCount];
  node* curNode = X.first;
  for (int i = 0; i < strCount; i++) {
    Y[i] = curNode->data * coef;
    curNode = curNode->next;
  }
  makerZ(Y, strCount);
  return Y;
}

float* makerZ(float* Y, int strCount) {
  list Y_;
  ifstream fin;
  fin.open("Y~.txt");
  string str = "";
  getline(fin, str);
  Y_.first = new node(atof(str.c_str()));
  Y_.last = Y_.first;
  while (!fin.eof()) {
    str = "";
    getline(fin, str);
    if (str.size()) {
      Y_.last->next = new node(atof(str.c_str()));
      Y_.last = Y_.last->next;
    }
  }
  float* Z = new float[strCount];
  for (int i = 0; i < strCount; i++) {
    node* curNode = Y_.first;
    bool OK = false;
    while(curNode->next != NULL) {
      if (curNode->data > Y[i] && Y[i] > curNode->next->data) {
        OK = true;
        if (Y[i] < (curNode->data + curNode->next->data) / 2) {
          Z[i] = curNode->next->data;
        } else {
          Z[i] = curNode->data;
        }
      }
      curNode = curNode->next;
    } 
    if (!OK) {
      Z[i] = Y[i];
    }
  }
  return Z;
}

void output(float* Y, float* Z, int strCount) {
  ofstream a;
  a.open("Y.txt");
  ofstream b;
  b.open("Z.txt");
  for (int curElIndex = 0; curElIndex < strCount; curElIndex++) {
    a << Y[curElIndex] << endl;
    b << Z[curElIndex] << endl;
  }
  a.close();
  b.close();
}