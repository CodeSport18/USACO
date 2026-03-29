// https://usaco.org/index.php?page=viewproblem2&cpid=1467

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, a, b;
        cin >> n >> a >> b;

        vector<string> grid(n);
        for (int i = 0; i < n; i++) {
            cin >> grid[i];
        }

        // count all non-white cells
        int totalStars = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != 'W') {
                    totalStars++;
                }
            }
        }

        // special case: no shift
        if (a == 0 && b == 0) {
            cout << totalStars << endl;
            continue;
        }

        // this will track which stars are "removed"
        vector<vector<bool>> removed(n, vector<bool>(n, false));

        // first pass: try to match forward (shift by +a, +b)
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {

                if (grid[r][c] == 'W') continue;
                if (removed[r][c]) continue;

                int nr = r + b;
                int nc = c + a;

                if (nr < n && nc < n) {
                    if (grid[nr][nc] != 'W') {
                        // only remove if it's not black
                        if (grid[nr][nc] != 'B') {
                            removed[nr][nc] = true;
                        }
                    }
                }
            }
        }

        // second pass: validate all black cells
        bool bad = false;

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {

                if (grid[r][c] != 'B') continue;

                int pr = r - b;
                int pc = c - a;

                // must have come from somewhere
                if (pr < 0 || pc < 0 || grid[pr][pc] == 'W') {
                    bad = true;
                    break;
                }

                // undo removal if needed
                if (removed[pr][pc]) {
                    removed[pr][pc] = false;
                }
            }

            if (bad) break;
        }

        if (bad) {
            cout << -1 << endl;
            continue;
        }

        // count how many were removed
        int removedCount = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (removed[r][c]) {
                    removedCount++;
                }
            }
        }

        int answer = totalStars - removedCount;
        cout << answer << endl;
    }
}