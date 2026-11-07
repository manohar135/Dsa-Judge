// Judge harness - reads stdin, calls your Solution, prints the result. Do not edit.
#include "solution.cpp"
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string a, b; std::cin >> a >> b;
    std::cout << Solution().minMergeInversions(a, b) << "\n";
    return 0;
}
