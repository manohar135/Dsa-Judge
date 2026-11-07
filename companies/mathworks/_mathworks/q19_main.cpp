// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string s; int l, r; std::cin >> s >> l >> r;
    std::cout << Solution().getShiftedString(s, l, r) << "\n";
    return 0;
}
