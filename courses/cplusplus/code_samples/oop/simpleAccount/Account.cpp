#include "Account.h"

using std::vector;
using std::string;
using std::to_string;

Account::Account() : balance(0), limit(100) 
{
}

std::vector<std::string> Report() {
  vector<string> report; 

  report.push_back("Balance is " + to_string(balance));
  report.push_back("Transactions: ");

  for (auto t : log) {
    report.push_back(t.Report());
  }

  report.push_back("-------");


  return report; 

}
