#include <iostream>
#include <vector>

//The function should return an std::vector of the first three multiples of num in ascending order.
// Define first_three_multiples() here:
std::vector<int> first_three_multiples(int num) {
  
  std::vector<int> multiples{num, num * 2, num * 3};
  
  return multiples;
  
}

int main() {
  
  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }
  
}