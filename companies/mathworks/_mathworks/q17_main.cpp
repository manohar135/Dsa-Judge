// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; long long T; std::cin >> n >> T;
    std::vector<int> p(n); for (auto& x : p) std::cin >> x;
    std::cout << Solution().maxCompletedProcesses(p, T) << "\n";
    return 0;
}
