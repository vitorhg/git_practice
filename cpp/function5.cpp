#include <iostream>
#include <cmath>

//The function should return num raised to the 10th power.
// Define tenth_power() here:
int tenth_power(int num) {
  
  return pow(num, 10);
  
}

int main() {
  
  std::cout << tenth_power(0) << "\n";
  std::cout << tenth_power(1) << "\n";
  std::cout << tenth_power(2) << "\n";
  
}