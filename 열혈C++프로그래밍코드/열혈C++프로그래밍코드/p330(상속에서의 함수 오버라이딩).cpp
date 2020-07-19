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
		std::cout << "PermanentWorker�� GetPay()" << std::endl;
		return 1;
	}
	void ShowSalaryInfo() const
	{
		std::cout << "PermanentWorker�� ShowSalaryInfo()" << std::endl; 
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
		//������� GetPay�Լ��� ȣ���Ͽ��� �� SalesWorker(Base class)�� GetPay�Լ��� ȣ�������
		//PermanentWorker��� �̸��� ��������ν� PermanentWorker(Derived class)�� GetPay�Լ��� ȣ���̵�
		std::cout << "SalesWorker�� GetPay()" << std::endl;
		return PermanentWorker::GetPay()+3;
	}
	//ShowSalaryInfo�� Overriding ���� ���� ����
	//Overriding�� ���� ������ SalesWorker�� ��ӵ� PermanentWorker�� ShowSalaryInfo�Լ��� ȣ��ǰ� ����
	//�� �ȿ� �ִ� PermanentWorker�� GetPay�Լ��� ȣ���
	//�׷��� ������ ShowSalaryInfo�Լ��� Overriding�Ͽ� SalesWorker�� GetPay�Լ��� ȣ����
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

