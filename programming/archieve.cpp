#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream input ("eurovision.csv", ifstream::binary);
  filebuf *buf = input.rdbuf();

  int size = buf->pubseekoff(0, input.end, input.in);

  char *buffer;
  for (int pos = 0; pos < size; ++pos) {
    buf->pubseekpos(pos, input.in);
    buffer = new char[1];
    buf->sgetn(buffer, 1);
    cout << int(buffer[0]) << " ";
    delete[] buffer;
  }

  input.close();
  cout << size << endl;
}
