#include <iostream>

auto check_bit(int num, int i) {
    return (num & (1 << i)) != 0;
}
auto set_bit(int num, int i) {
    return (num | (1 << i));
}
auto main() -> int {if (check_bit(0b1010101, 2)) {std::cout << "SET\n";} else {std::cout << "NOT SET\n"; }if (check_bit(0b1010101, 5)) {std::cout << "SET\n";} else {std::cout << "NOT SET\n"; }return 0;}
