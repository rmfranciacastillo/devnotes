/**
 * Shows the limit size of datatypes 
 */ 
#include <iostream>
#include <limits>

using namespace std; 

void comma_datatype();

int main() {
  
  cout << "The range for type short is from " 
       << std::numeric_limits<short>::min() << " to "
       << std::numeric_limits<short>::max() << endl;

  comma_datatype();
  
  return 0;
}

void comma_datatype() {
   
  int i {1};
  int value1 {1};
  int value2 {1};
  int value3 {1};

  cout << (value1 += ++i, value2 += ++i, value3 += ++i) << endl;
}
