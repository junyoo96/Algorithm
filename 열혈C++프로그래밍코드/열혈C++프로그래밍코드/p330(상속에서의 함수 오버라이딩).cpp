#include <iostream>

class Employee
{

public:
	Employee()
	{

	}
	void ShowYourName() const
	{

	}
};

class PermanentWorker : public Employee
{
public:
	PermanentWorker()
	{

	}
	int GetPay() const
	{
		std::cout << "PermanentWorker의 GetPay()" << std::endl;
		return 1;
	}
	void ShowSalaryInfo() const
	{
		std::cout << "PermanentWorker의 ShowSalaryInfo()" << std::endl; 
	}
};

class SalesWorker : public PermanentWorker
{
public:
	SalesWorker()
	{

	}
	void AddSalesResult()
	{

	}
	int GetPay() const
	{
		//원래라면 GetPay함수를 호출하였을 때 SalesWorker(Base class)의 GetPay함수가 호출되지만
		//PermanentWorker라고 이름을 명시함으로써 PermanentWorker(Derived class)의 GetPay함수가 호출이됨
		std::cout << "SalesWorker의 GetPay()" << std::endl;
		return PermanentWorker::GetPay()+3;
	}
	//ShowSalaryInfo를 Overriding 하지 않은 이유
	//Overriding을 하지 않으면 SalesWorker에 상속된 PermanentWorker의 ShowSalaryInfo함수가 호출되고 따라서
	//그 안에 있는 PermanentWorker의 GetPay함수가 호출됨
	//그렇기 때문에 ShowSalaryInfo함수를 Overriding하여 SalesWorker의 GetPay함수를 호출함
	void ShowSalaryInfo() const
	{
		ShowYourName();
		std::cout << "salary :" << GetPay() << std::endl;
	}
};

int main(void)
{
	SalesWorker sal;
	sal.ShowSalaryInfo();
	sal.PermanentWorker::GetPay();
	
	

}

