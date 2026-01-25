#include <iostream>
#include <vector>
#include <unordered_map>

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
            start += 1;
        }
    }

    // Odd-subarray length iteration
    for (int i = 0; i < number_of_cows; ++i) {
        int left = i;
        int right = i;

        int answer = start;

        while (left >= 0 && right < number_of_cows) {
            if (cow_line[left] == wanted_cow_line[right]) {
                answer += 1;
            }
            if (cow_line[right] == wanted_cow_line[left]) {
                answer += 1;
            }
            if (cow_line[left] == wanted_cow_line[left]) {
                answer -= 1;
            }
            if (cow_line[right] == wanted_cow_line[right]) {
                answer -= 1;
            }

            answers[answer] += 1;

            --left;
            ++right;
        }
    }

    // Even-subarray length iteration
    for (int i = 1; i < number_of_cows; ++i) {
        int left = i - 1;
        int right = i;

        int answer = start;

        while (left >= 0 && right < number_of_cows) {
            if (cow_line[left] == wanted_cow_line[right]) {
                answer += 1;
            }
            if (cow_line[right] == wanted_cow_line[left]) {
                answer += 1;
            }
            if (cow_line[left] == wanted_cow_line[left]) {
                answer -= 1;
            }
            if (cow_line[right] == wanted_cow_line[right]) {
                answer -= 1;
            }

            answers[answer] += 1;

            --left;
            ++right;
        }
    }

    for (int number = 0; number <= number_of_cows; ++number) {
        std::cout << answers[number] << "\n";
    }

    return 0;
}