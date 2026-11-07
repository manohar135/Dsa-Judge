// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k; std::cin >> n >> k;
    std::vector<std::vector<int>> b(n, std::vector<int>(2));
    for (auto& v : b) std::cin >> v[0] >> v[1];
    std::cout << Solution().earliestFreeStart(b, k) << "\n";
    return 0;
}
