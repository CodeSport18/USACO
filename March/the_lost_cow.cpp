#include <iostream>
using namespace std;

int main() {
    freopen("lostcow.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("lostcow.out", "w", stdout);

    int x,y;
    cin >> x >> y;
    bool z = (x<y);
    int initial_x = x;
    int increment = 1;
    int to_add = 1;
    int distance = 0;

    if (z == 1) {
        while (true) {
            if (x >= y) {
                break;
            }
            distance += abs(x-(increment+initial_x));
            x = (increment+initial_x);
            // to_add = abs(increment*3);
            increment *= -2;
        }
    }

    else {
        while (true) {
            if (x <= y) {
                break;
            }
            distance += abs(x-(increment+initial_x));
            x = (increment+initial_x);
            // to_add = abs(increment*3);
            increment *= -2;
        }
    }

    cout << (distance-abs(y-x)) << endl;

}