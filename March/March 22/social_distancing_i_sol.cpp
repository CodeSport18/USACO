// https://usaco.org/index.php?page=viewproblem2&cpid=1035

#include <iostream>
#include <fstream>
using namespace std;
 
// Returns size of largest gap between two 1s and also the index where it starts
int find_largest_interior_gap(string stalls, int &gap_start)
{
  int biggest_gap = 0, current_start = -1, N = stalls.length();
  for (int i=0; i<N; i++) 
    if (stalls[i] == '1') {
      if (current_start!=-1 && i-current_start > biggest_gap) {
	biggest_gap = i-current_start;
	gap_start = current_start;
      }
      current_start = i;
    }
  return biggest_gap;
}
 
// Returns size of smallest gap between two 1s
int find_smallest_interior_gap(string stalls)
{
  int smallest_gap = 1000000000, current_start = -1, N = stalls.length();
  for (int i=0; i<N; i++) 
    if (stalls[i] == '1') {
      if (current_start!=-1 && i-current_start < smallest_gap) smallest_gap = i-current_start;
      current_start = i;
    }
  return smallest_gap;
}
 
int try_cow_in_largest_gap(string stalls)
{
  int gap_start, largest_gap = find_largest_interior_gap(stalls, gap_start);
  if (largest_gap >= 2) {
    stalls[gap_start + largest_gap / 2] = '1';
    return find_smallest_interior_gap(stalls);
  } 
  return -1; // no gap!
}
 
int main(void)
{
  ifstream fin ("socdist1.in");
  int N;
  string stalls, temporary_stalls;
  fin >> N >> stalls;
  ofstream fout ("socdist1.out");
  int answer = 0;
 
  // Possibility 1. put two cows in largest interior gap
  int gap_start, largest_gap = find_largest_interior_gap(stalls, gap_start);
  if (largest_gap >= 3) {
    temporary_stalls = stalls;
    temporary_stalls[gap_start + largest_gap / 3] = '1';
    temporary_stalls[gap_start + largest_gap * 2 / 3] = '1';
    answer = max(answer, find_smallest_interior_gap(temporary_stalls));
  }
 
  // Possibility 2. cows at both ends
  if (stalls[0] == '0' && stalls[N-1] == '0') {
    temporary_stalls = stalls; temporary_stalls[0] = temporary_stalls[N-1] = '1';
    answer = max(answer, find_smallest_interior_gap(temporary_stalls));        
  }
 
  // Possibility 3. cow at left + cow in largest interior gap
  if (stalls[0] == '0') {
    temporary_stalls = stalls; temporary_stalls[0] = '1';
    answer = max(answer, try_cow_in_largest_gap(temporary_stalls));
  }
 
  // Possibility 4. cow at right + cow in largest interior gap
  if (stalls[N-1] == '0') {
    temporary_stalls = stalls; temporary_stalls[N-1] = '1';
    answer = max(answer, try_cow_in_largest_gap(temporary_stalls));
  }
 
  // Possibility 5. cow at largest interior gap.  done twice.
  if (largest_gap >= 2) {
    temporary_stalls = stalls; temporary_stalls[gap_start + largest_gap / 2] = '1';
    answer = max(answer, try_cow_in_largest_gap(temporary_stalls));
  }
 
  fout << answer << "\n";
  return 0;
}