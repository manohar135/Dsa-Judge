// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; std::cin >> n;
    std::vector<std::string> v(n); for (auto& s : v) std::cin >> s;
    std::vector<long long> r = Solution().countScatterPalindromes(v);
    for (long long x : r) std::cout << x << "\n";
    return 0;
}
