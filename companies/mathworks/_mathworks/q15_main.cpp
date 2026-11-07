// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string s; int m; std::cin >> s >> m;
    std::vector<int> a(m); for (auto& x : a) std::cin >> x;
    std::cout << Solution().applyReversals(s, a) << "\n";
    return 0;
}
