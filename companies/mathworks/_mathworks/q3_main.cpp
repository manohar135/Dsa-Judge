// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; std::cin >> n;
    std::vector<int> a(n); for (auto& x : a) std::cin >> x;
    std::vector<long long> r = Solution().sumOfDivisors(a);
    std::string out; for (long long v : r) { out += std::to_string(v); out += '\n'; }
    std::cout << out;
    return 0;
}
