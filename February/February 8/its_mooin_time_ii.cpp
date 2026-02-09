#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>

int main() {
    int num_of_integers;
    std::cin >> num_of_integers;

    std::vector<int> the_integers(num_of_integers);
    for (int i = 0; i < num_of_integers; ++i) {
        std::cin >> the_integers[i];
    }

    std::unordered_map<int, int> first_occurrences;
    std::unordered_map<int, int> last_single_occurrences;
    std::unordered_map<int, int> last_double_occurrences;

    for (int integer_index = 0; integer_index < num_of_integers; ++integer_index) {
        if (first_occurrences.find(the_integers[integer_index]) == first_occurrences.end()) {
            first_occurrences[the_integers[integer_index]] = integer_index;
        }
    }

    for (int integer_index = num_of_integers - 1; integer_index >= 0; --integer_index) {
        int val = the_integers[integer_index];
        if (last_double_occurrences.find(val) == last_double_occurrences.end()) {
            if (last_single_occurrences.find(val) != last_single_occurrences.end() &&
                last_double_occurrences.find(val) == last_double_occurrences.end()) {
                last_double_occurrences[val] = integer_index;
            }
        }
        last_single_occurrences[val] = integer_index;
    }

    // Sort last_single_occurrences by value (index)
    std::map<int, int> first_single_occurrences;
    for (const auto& p : last_single_occurrences) {
        first_single_occurrences[p.first] = p.second;
    }
    // Sorting by value, so we create a vector and sort it
    std::vector<std::pair<int, int>> sorted_first_single_occurrences(first_single_occurrences.begin(), first_single_occurrences.end());
    std::sort(sorted_first_single_occurrences.begin(), sorted_first_single_occurrences.end(),
              [](const std::pair<int,int>& a, const std::pair<int,int>& b) {
                  return a.second < b.second;
              });

    // Sort last_double_occurrences by value (index)
    std::vector<std::pair<int, int>> sorted_last_double_occurrences(last_double_occurrences.begin(), last_double_occurrences.end());
    std::sort(sorted_last_double_occurrences.begin(), sorted_last_double_occurrences.end(),
              [](const std::pair<int,int>& a, const std::pair<int,int>& b) {
                  return a.second < b.second;
              });

    // Extract keys from sorted_last_double_occurrences
    std::vector<int> keys;
    for (const auto& p : sorted_last_double_occurrences) {
        keys.push_back(p.first);
    }

    int num_of_os = static_cast<int>(keys.size());
    int counter = 0;

    // We'll use an index to track the start of keys vector since we remove from front
    int start_idx = 0;

    for (const auto& m_pair : sorted_first_single_occurrences) {
        int m = m_pair.first;
        int m_val = m_pair.second;

        while (start_idx < num_of_os && sorted_last_double_occurrences[start_idx].second < m_val) {
            ++start_idx;
        }

        int current_num_of_os = num_of_os - start_idx;
        counter += current_num_of_os;

        // Check if m is in last_double_occurrences
        // Since last_double_occurrences is unordered_map, check directly
        if (last_double_occurrences.find(m) != last_double_occurrences.end()) {
            counter -= 1;
        }
    }

    std::cout << counter << std::endl;

    return 0;
}