// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, lo, hi; std::cin >> n >> lo >> hi;
    std::vector<int> a(n); for (auto& x : a) std::cin >> x;
    std::cout << Solution().countSubarrays(a, lo, hi) << "\n";
    return 0;
}
