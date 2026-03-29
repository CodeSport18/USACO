// https://usaco.org/index.php?page=viewproblem2&cpid=1035

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional> // for std::greater
using namespace std;

int main() {
    freopen("socdist1.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("socdist1.out", "w", stdout);

    int n;
    cin >> n;

    string stalls;
    cin >> stalls;

    int the_index = 0;
    int count = 1;
    
    // int gaps[n] = {};
    std::vector<int> gaps(n, 0);

    for (int i = 0; i < n; i++) {
        if (stalls[i] == '0') {
            count += 1;
        }
        else if (count > 1) {
            gaps[the_index] = count;
            count = 1;
            the_index += 1;
        }
    }

    int start_gap = 0;
    int end_gap = 0;

    if (count > 1) {
        int end_gap = count;
        count = 1;
        // the_index += 1;
        // cout << end_gap << endl;
    }    



    if (stalls[0] == '0') {
        int start_gap = gaps[0];
        gaps.erase(gaps.begin() + 0);
        the_index -= 1;
        if (the_index == 0) {

        }
        // cout << start_gap << endl;
    }

    std::vector<int>::iterator max_it = std::max_element(gaps.begin(), gaps.end());
    // Dereference the iterator to get the actual maximum value
    int max_value = *max_it;
    int alternative = max_value / 3;

    int min_value = -1;
    for (int i = 0; i < n; i++) {
        if (min_value == -1 and gaps[i] > 0) {
            min_value = gaps[i];
        }
        else if (gaps[i] < min_value and gaps[i] > 0) {
            min_value = gaps[i];
        }
    }

    if (min_value < alternative and min_value > 0) {
        alternative = min_value;
    }
    



    for (int i = 0; i < 2; i++) {
        std::sort(gaps.begin(), gaps.end(), std::greater<int>());

        // for (int i = 0; i < n; i++) {
        //     cout << gaps[i];
        // }
        // cout << endl;

        int gapOne = gaps[0] / 2;
        int gapTwo = gaps[0] - gapOne;

        if (gapOne > start_gap and gapOne > end_gap) {
            gaps[0] = gapOne;
            gaps[the_index] = gapTwo;
            the_index += 1;
    
            // for (int i = 0; i < n; i++) {
            //     cout << gaps[i];
            // }
            // cout << endl;
        }

        else {

            if (start_gap > end_gap) {
                gaps[the_index] = start_gap;
            }

            else {
                gaps[the_index] = end_gap;
            }

            the_index += 1;
    
            // for (int i = 0; i < n; i++) {
            //     cout << gaps[i];
            // }
            // cout << endl;
        }
        
    }

    std::sort(gaps.begin(), gaps.end());

    int last = 0;

    for (int i = 0; i < n; i++) {
        if (gaps[i] > 0) {
            if (alternative > gaps[i]) {
                cout << alternative << endl;
                last = alternative;
            }
            else {
                cout << gaps[i] << endl;
                last = gaps[i];
            }
            break;
        }
    }

    if (last == 0) {
        cout << alternative << endl;
    }

}