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

	vector<int> arr(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	int cost(0);
	for (int i = 0; i < n-1; i++) {
		if (arr[i] > arr[i + 1]) {
			cost += arr[i] - arr[i + 1];
		}
	}

	cout << cost;

	return 0;
}
