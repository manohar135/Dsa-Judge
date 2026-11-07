// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k; std::cin >> n >> k;
    std::vector<int> arr(n); for (auto& x : arr) std::cin >> x;
    std::cout << Solution().findLeastNumOfUniqueInts(arr, k) << "\n";
    return 0;
}
