#include <iostream>
using namespace std;

bool ok(int q[], int c) {
  for (int i = 0; i < c; i++) {
    if ((q[c] == q[i] || ((c - i) == abs(q[c] - q[i])))) return false;
  }
  return true;
}
void print(int q[]) {
  //counter++;
  for (int r = 0; r < 8; r++) {
    for (int c = 0; c < 8; c++) {
      if (q[c] == r) cout << "1" << " ";
      else cout << "0" << " ";
    }
    cout << endl;
 }
 cout << "Solution #" << endl;
}

void backtrack(int &c) {
  c--;
  if (c == -1) exit (0);
}

int main () {
  int c = 0, q[8];
  q[0] = 0;
  while (c != -1) {
    c++; // next column
    if (c == 8) {
      print(q);
      backtrack(c);
      return 0;
    }
    else q[c] = -1;
    while (c != -1) {
      q[c]++;
      if (q[c] == 8) backtrack(c);
      else if (ok(q, c) == true) break;
    }
  }

return 0;
}