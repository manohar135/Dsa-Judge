// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string s; std::cin >> s;
    std::cout << Solution().maxBeautifulSubstrings(s) << "\n";
    return 0;
}
