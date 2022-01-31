#include <vector>
#include <string>
#include "Transaction.h"

class Account {
  private:
    int balance;
    std::vector<Transaction> log;
    int limit;

  public:
    Account();
    std::vector<std::string> Report();
    bool Deposit(int amount);
    bool Withraw(int amount);
    int GetBalance() { return balance; }
};
