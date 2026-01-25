#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

int main() {
    int number_of_cows;
    std::cin >> number_of_cows;

    std::vector<int> cow_line(number_of_cows);
    std::vector<int> wanted_cow_line(number_of_cows);

    for (int i = 0; i < number_of_cows; ++i) {
        std::cin >> cow_line[i];
    }
    for (int i = 0; i < number_of_cows; ++i) {
        std::cin >> wanted_cow_line[i];
    }

    std::unordered_map<int, int> answers;

    int start = 0;
    for (int cow_index = 0; cow_index < number_of_cows; ++cow_index) {
        if (wanted_cow_line[cow_index] == cow_line[cow_index]) {
            ++start;
        }
    }

    for (int l = 0; l < number_of_cows; ++l) {
        for (int r = l; r < number_of_cows; ++r) {
            int answer = start;
            std::vector<int> cow_line_copy = cow_line;

            for (int cow_index = l; cow_index <= r; ++cow_index) {
                if (wanted_cow_line[cow_index] == cow_line_copy[cow_index]) {
                    --answer;
                }
            }

            std::reverse(cow_line_copy.begin() + l, cow_line_copy.begin() + r + 1);

            for (int cow_index = l; cow_index <= r; ++cow_index) {
                if (wanted_cow_line[cow_index] == cow_line_copy[cow_index]) {
                    ++answer;
                }
            }

            ++answers[answer];
        }
    }

    for (int number = 0; number <= number_of_cows; ++number) {
        std::cout << answers[number] << "\n";
    }

    return 0;
}