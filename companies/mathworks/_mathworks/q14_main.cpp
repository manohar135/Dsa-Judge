// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, q; std::cin >> n >> q;
    std::vector<int> b(n), a(q); for (auto& x : b) std::cin >> x; for (auto& x : a) std::cin >> x;
    std::vector<int> r = Solution().finalBulbStates(b, a);
    std::string out; for (int v : r) { out += std::to_string(v); out += '\n'; }
    std::cout << out;
    return 0;
}
