// Still TLE

#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
#define MAX 500001
#define vi vector<int>
#define pb push_back
#include <algorithm>
vi graph[MAX];
vi children[MAX];
vi parents[MAX];
int vis[MAX] = {0};
int downmemo[MAX] = {0};
int upmemo[MAX] = {0};
int downmemo2[MAX] = {0};
int bestused[MAX] = {0};

void dfs(int n){
    vis[n] = 1;
    for (int node : graph[n]){
        if (vis[node] == 0){
            children[n].pb(node);
            parents[node].pb(n);
            dfs(node);
        }
    }
}

tuple<int, int> downdp(int k){
    int best = 0;
    int secondbest = 0;
    if (downmemo[k] != 0 && downmemo2[k] != 0){
        return make_tuple(downmemo[k], downmemo2[k]);
    }
    for (int node : children[k]){
        auto [ans, useless] = downdp(node);
        ans += 1;
        if (ans > best){
            if (best > secondbest){
                secondbest = best;
            }
            best = ans;
            bestused[k] = node;
        }
        else {
            if (ans > secondbest){
                secondbest = best;
            }
        }
    }
    downmemo[k] = best;
    downmemo2[k] = secondbest;
    return make_tuple(best, secondbest);
}
int updp(int k){
    int up = 0;
    if (upmemo[k] != 0){
        return upmemo[k];
    }
    for (auto parent : parents[k]){
        auto [down1, down2] = downdp(parent);
        if (bestused[parent] == k){
            up = down2+1;
        }
        else {
            up = down1+1;
        }
        up = max(up, 1 + updp(parent));
    }
    upmemo[k] = up;
    return up;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n-1; i++){
        int u; int v;
        cin >> u;
        cin >> v;
        graph[u].pb(v);
        graph[v].pb(u);
    }
    dfs(1);
    for (int i=1; i<=n; i++){
        auto [x, y] = downdp(i);
        cout << max(x, updp(i))+1 << "\n";
    }
}