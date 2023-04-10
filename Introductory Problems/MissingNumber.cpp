#include <iostream>
#include <vector>
#include <sstream>
#include <stack>
#include <deque>
#include <string>
#include <numeric>

using namespace std;

int main() {

	int n;
	cin >> n;

	vector<int> arr(n-1);
	for (int i = 0; i < n-1; i++) {
		cin >> arr[i];
	}

	int miss;
	miss = (n * (n + 1)) / 2 - accumulate(arr.begin(), arr.end(), 0);

	cout << miss;

	return 0;
}
