// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string s; int k; std::cin >> s >> k;
    std::vector<int> r = Solution().consecutiveWindowDistances(s, k);
    std::string out; for (int v : r) { out += std::to_string(v); out += '\n'; }
    std::cout << out;
    return 0;
}
