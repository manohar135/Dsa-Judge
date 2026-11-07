// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, x, y, z; std::cin >> n >> x >> y >> z;
    std::vector<int> a(n); for (auto& v : a) std::cin >> v;
    std::cout << Solution().maxSumOfPieces(a, x, y, z) << "\n";
    return 0;
}
