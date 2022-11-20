#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int k;
    int n;
	cin >> n >> k;
    const int arr_size = 2e5 + 3;
    int items[arr_size];
    for(int i = 0; i < n; i++){
        cin >> items[i];
    }
    int ans;
    sort(begin(items), begin(items)+n);
    for (int i = 0; i < n; i++) {
        int e = lower_bound(begin(items), begin(items) + n, items[i] - k) - items;
        ans = max(ans, i - e + 1);
    }
    cout << ans;
    return 0;
}