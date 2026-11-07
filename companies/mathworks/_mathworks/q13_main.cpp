// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m, a, b, c; std::cin >> n >> m >> a >> b >> c;
    std::vector<std::vector<int>> e(m, std::vector<int>(3));
    for (auto& v : e) std::cin >> v[0] >> v[1] >> v[2];
    std::cout << Solution().minCostVia(n, e, a, b, c) << "\n";
    return 0;
}
