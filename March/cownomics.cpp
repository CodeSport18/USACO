#include <iostream>
using namespace std;

int main() {
    freopen("lostcow.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("lostcow.out", "w", stdout);

    int n,m;
    cin >> n >> m;

    for (int i = 0; i < n*2; i++) {
        cin << i << "\n";
    }
}