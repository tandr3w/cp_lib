#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int k;
    int n;
	cin >> n >> k;
    vector<int> items(n);
    for(int i = 0; i < n; i++){
        cin >> items[i];
    }
    if (n == 2){
        if (items.back() - items[0] <= k){
            cout << 2;
        }
        else {
            cout << 1;
        }
    }
    else {
        sort(items.begin(), items.end());
        int best = 1;
        for (int j = 0; j < n-1; j++){
            if (n-j < best){
                break;
            }
            int x = 0;
            int m = n-j-1;
            while (m != 1){
                m /= 2;
                while ((x + m < n-j) && (items[x+m] - items[0] <= k)){
                    x += m;
                }
            }
            best = max(best, x+1);
            items.erase(items.begin());
        }
        cout << best << endl;
    }
    return 0;
}