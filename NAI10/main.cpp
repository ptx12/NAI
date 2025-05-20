#include <iostream>
#include <chrono>

const int N = 32;
int weights[N] = {
        3, 1, 6, 10, 1, 4, 9, 1,
        7, 2, 6, 1, 6, 2, 2, 4,
        8, 1, 7, 3, 6, 2, 9, 5,
        3, 3, 4, 7, 3, 5, 30, 50
};
int values[N] = {
        7, 4, 9, 18, 9, 15, 4, 2,
        6, 13, 18, 12, 12, 16, 19, 19,
        10, 16, 14, 3, 14, 4, 15, 7,
        5, 10, 10, 13, 19, 9, 8, 5
};
int W_max = 75;

int main() {
    std::size_t bestMask = 0;
    int bestValue = 0;
    int bestWeight = 0;

    auto start = std::chrono::high_resolution_clock::now();
    for (std::size_t mask = 0; mask < (1ULL << N); ++mask) {
        int w = 0, v = 0;
        for (std::size_t i = 0; i < N; ++i) {
            if (mask & (1ULL << i)) {
                w += weights[i];
                v += values[i];
                if (w > W_max) break;
            }
        }
        if (w <= W_max && v > bestValue) {
            bestValue = v;
            bestWeight = w;
            bestMask = mask;
            std::cout << "new best value found: " << bestValue << "|" << bestWeight << " - " << std::chrono::duration<double>(std::chrono::high_resolution_clock::now() - start).count() << std::endl;
        }
    }
    auto end = std::chrono::high_resolution_clock::now();
    double elapsed = std::chrono::duration<double>(end - start).count();

    std::cout << "ELAPSED TIME:   " << elapsed << "\n";
    std::cout << "TOTAL WEIGHT:   " << bestWeight << "\n";
    std::cout << "TOTAL VALUE:    " << bestValue << "\n";
    std::cout << "MASK:           ";
    for (std::size_t i = N; i > 0; --i) {
        std::cout << ((bestMask >> (i - 1)) & 1);
    }
}