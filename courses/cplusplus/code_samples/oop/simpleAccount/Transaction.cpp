#include "Transaction.h"

using std::string;
using std::to_string;

Transaction::Transaction(int amt, std::string kind) : amount(amt), type(kind) 
{
}

std::string Transaction::Report()
{

  string report; 
  report += "  ";
  report += type;
  report += "  ";
  report += to_string(amount);

  return report; 
}
