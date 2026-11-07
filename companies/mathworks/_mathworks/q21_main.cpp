// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; std::cin >> n;
    std::vector<int> e(n), d(n); for (auto& x : e) std::cin >> x; for (auto& x : d) std::cin >> x;
    std::cout << Solution().minOperations(e, d) << "\n";
    return 0;
}
