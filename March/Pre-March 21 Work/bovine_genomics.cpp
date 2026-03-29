// https://usaco.org/index.php?page=viewproblem2&cpid=736

#include <iostream>
using namespace std;

int main() {
    freopen("cownomics.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("cownomics.out", "w", stdout);

    int n,m;
    cin >> n >> m;
    string good_genomes[n];
    string bad_genomes[n];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> good_genomes[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> bad_genomes[i][j];
        }
    }

    int counter = 0;

    for (int i = 0; i < m; i++) {

        bool can_be_done = true;

        for (int j = 0; j < n; j++) {

            for (int k = 0; k < n; k++) {
                if (good_genomes[j][i] == bad_genomes[k][i]) {
                    // cout << good_genomes[j][i] << bad_genomes[k][i] << endl;
                    can_be_done = false;
                    break;
                };
            }

            if (can_be_done == false) {
                break;
            }
            
        }

        if (can_be_done == true) {
            counter += 1;
        }
    }
    
    cout << counter << endl;
}