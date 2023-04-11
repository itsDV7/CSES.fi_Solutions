#include <iostream>
#include <vector>
#include <sstream>
#include <stack>
#include <deque>
#include <string>
#include <numeric>

using namespace std;

int main() {

	int t;
	cin >> t;

	int r, c;
	int rs, cs;
	while (t) {
		cin >> r >> c;
		if (r % 2) {
			rs = ((r - 1) * (r - 1)) + 1;
		}
		else {
			rs = r * r;
		}
		if (c % 2) {
			cs = c * c;
		}
		else {
			cs = ((c - 1) * (c - 1)) + 1;
		}

		if (c >= r && cs % 2 == 0) {
			cout << cs + r - 1 << " ";
		}
		else if (c > r && cs % 2 != 0) {
			cout << cs - r + 1 << " ";
		}
		else if (c < r && cs % 2 == 0) {
			cout << rs - c + 1 << " ";
		}
		else {
			cout << rs + c - 1 << " ";
		}
		t -= 1;
	}

	return 0;
}
