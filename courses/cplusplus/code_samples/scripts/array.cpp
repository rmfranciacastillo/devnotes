/*
 * Types of arrays
 */
#include <iostream>
#include <array>

using namespace std; 

int main() {

  array<double, 10> values {}; // create an array of 10 double values

  // Fill all values with random stuff
  values.fill(3.1416)

  return 0;
}
