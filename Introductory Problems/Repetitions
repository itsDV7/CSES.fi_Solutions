#include <iostream>
#include <vector>
#include <sstream>
#include <stack>
#include <deque>
#include <string>
#include <numeric>

using namespace std;

int main() {

	string s;
	getline(cin, s);

	vector<char> arr(s.begin(), s.end());

	int count(1);
	int max_count(-1);
	for (int i = 0; i < arr.size() - 1; i++) {
		if (arr[i] == arr[i + 1]) {
			count += 1;
		}
		else {
			max_count = max(max_count, count);
			count = 1;
		}
	}
	
	cout << max_count;

	return 0;
}
