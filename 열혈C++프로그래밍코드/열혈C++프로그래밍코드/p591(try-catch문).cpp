#include<iostream>

int main(void)
{
	int num1, num2;
	std::cout << "�� ���� �����Է�:" << std::endl;
	std::cin >> num1 >> num2;

	try
	{
		if (num2 == 0)
		{
			throw num2;
		}
		std::cout << "�������� ��: " << num1 / num2 << std::endl;
		std::cout << "�������� ������: " << num1 % num2 << std::endl;
	}
	catch(int expn)
	{
		std::cout << "������ " << expn << "�� �ɼ������ϴ�." << std::endl;
		std::cout << "���α׷� �ٽ� �����ض�" << std::endl;
	}

	std::cout << "end of main" << std::endl;
	return 0;
}

int SimpleFunc(void) throw ()
{
	try
	{
		if (true)
		{
			throw 'A';
		}
	}
	catch (char expn)
	{

	}
	catch (int expn2)
	{

	}
}