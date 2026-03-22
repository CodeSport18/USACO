#include <iostream>

void set_up(std::string name) {
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
}

int main() {
	set_up("paint");
	int a, b, c, d;
	std::cin >> a >> b >> c >> d;

	if (a <= c) {
		if (b < c) {
			std::cout << b - a + d - c;
		} else if (b < d) {
			std::cout << d - a;
		} else {
			std::cout << b - a;
		}
	} else {
		if (d < a) {
			std::cout << b - a + d - c;
		} else if (d < b) {
			std::cout << b - c;
		} else {
			std::cout << d - c;
		}
	}
}