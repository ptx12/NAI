#include <iostream>
#include <chrono>

auto generate_neighbours(long solution, int n) -> std::vector<long>
{
    std::vector<long> result;
    for (int i = 0; i < n; i++) {
        result.push_back(solution ^ (1 << i));
    }
    return result;
}
auto main() -> int {
    for (auto element : generate_neighbours(0b1010,4)) {
        std::cout << element << std::endl;
    }
}