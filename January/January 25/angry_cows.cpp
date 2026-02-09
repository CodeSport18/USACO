#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream file_in("angry.in");
    int number_of_bales;
    file_in >> number_of_bales;

    std::vector<int> bales(number_of_bales);
    for (int i = 0; i < number_of_bales; ++i) {
        file_in >> bales[i];
    }
    file_in.close();

    std::sort(bales.begin(), bales.end());

    std::vector<int> bale_distances_from_left;
    int previous_bale = 0;
    for (int bale : bales) {
        bale_distances_from_left.push_back(bale - previous_bale);
        previous_bale = bale;
    }

    std::reverse(bales.begin(), bales.end());

    std::vector<int> bale_distances_from_right;
    previous_bale = 0;
    for (int bale : bales) {
        bale_distances_from_right.push_back(previous_bale - bale);
        previous_bale = bale;
    }
    std::reverse(bale_distances_from_right.begin(), bale_distances_from_right.end());
    std::reverse(bales.begin(), bales.end());

    int max_possibility = 0;

    if (number_of_bales >= 3) {
        for (int bale_index = 1; bale_index < number_of_bales - 1; ++bale_index) {
            int current_possibility = 1;

            // Check the bales going right
            for (int distance_index = bale_index + 1; distance_index < number_of_bales; ++distance_index) {
                if (bale_distances_from_left[distance_index] > (distance_index - bale_index)) {
                    break;
                }
                current_possibility += 1;
            }

            // Check the bales going left
            for (int distance_index = bale_index - 1; distance_index >= 0; --distance_index) {
                if (bale_distances_from_right[distance_index] > (bale_index - distance_index)) {
                    break;
                }
                current_possibility += 1;
            }

            if (current_possibility > max_possibility) {
                max_possibility = current_possibility;
            }
        }
    }

    std::ofstream file_out("angry.out");
    file_out << max_possibility;
    file_out.close();

    return 0;
}