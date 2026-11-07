// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; std::cin >> n;
    std::vector<int> a(n), b(n); for (auto& x : a) std::cin >> x; for (auto& x : b) std::cin >> x;
    std::cout << Solution().getMaxSumOfArray(a, b) << "\n";
    return 0;
}
