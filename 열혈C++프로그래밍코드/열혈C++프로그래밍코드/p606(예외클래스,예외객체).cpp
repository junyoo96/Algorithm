#include <iostream>
#include<cstring>

class AccountException
{
	void ShowExceptionReason()
	{

	}
};

class DepositExecption : public AccountException
{
private:
	int reqDep;
public:
	DepositExecption(int money) : reqDep(money)
	{		
	}
	void ShowExpectionReason()
	{
		std::cout << "예외 메시지 : " << reqDep << "는 입금불가" << std::endl;
	}		
};

class WithdrawExecption : public AccountException
{
private:
	int balance;
public:
	WithdrawExecption(int money) : balance(money)
	{
	}
	void ShowExpectionReason()
	{
		std::cout << "예외 메시지 : " << balance << "는 입금불가" << std::endl;
	}
};

class Account
{
private:
	char accNum[50];
	int balance;
public:
	Account(const char* acc, int money) : balance(money)
	{		
		strcpy_s(accNum,sizeof(accNum)/sizeof(accNum[0]), acc);
		std::cout << balance << std::endl;
	}
	void Deposit(int money) throw (AccountException)
	{
		if (money < 0)
		{
			DepositExecption expn(money);
			throw expn;
		}
		balance += money;
	}
	void Withdraw(int money) throw (AccountException)
	{
		if (money > balance)
		{
			throw WithdrawExecption(balance);
		}
		balance -= money;
	}
	void ShowMyMoney()
	{
		std::cout << "잔고: " << balance << std::endl;
	}
};

int main(void)
{
	Account myAcc("1234-5678", 15000);
	myAcc.ShowMyMoney();

	try
	{
		myAcc.Deposit(2000);
		myAcc.Deposit(-3000);
	}
	catch (DepositExecption& expn)
	{
		expn.ShowExpectionReason();
	}
	myAcc.ShowMyMoney();

	try
	{
		myAcc.Withdraw(3500);
		myAcc.Withdraw(4500);
	}
	catch(WithdrawExecption& expn)
	{
		expn.ShowExpectionReason();
	}
	myAcc.ShowMyMoney();
	return 0;
}