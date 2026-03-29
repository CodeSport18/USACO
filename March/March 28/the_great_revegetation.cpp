// https://usaco.org/index.php?page=viewproblem2&cpid=916

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

int main() {
    freopen("revegetate.in", "r", stdin);
    freopen("revegetate.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);

    // build graph (only store backwards edges)
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        a--;
        b--;

        int bigger = max(a, b);
        int smaller = min(a, b);

        adj[bigger].push_back(smaller);
    }

    int max_colors = 4;

    // color of each pasture
    vector<int> color(n, 1);

    for (int i = 0; i < n; i++) {

        // at most 3 neighbors already colored
        assert(adj[i].size() < max_colors);

        vector<bool> used(max_colors + 1, false);

        // mark colors that neighbors already use
        for (int neighbor : adj[i]) {
            int c = color[neighbor];
            used[c] = true;
        }

        // pick smallest available color
        while (used[color[i]]) {
            color[i]++;
        }

        cout << color[i];
    }

    cout << endl;
}