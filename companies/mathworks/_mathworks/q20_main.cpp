// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; std::cin >> n;
    std::vector<std::vector<int>> p(n, std::vector<int>(2));
    for (auto& v : p) std::cin >> v[0] >> v[1];
    std::cout << Solution().closestPairSquared(p) << "\n";
    return 0;
}
