#include<iostream>

int main(void)
{
	int num1, num2;
	std::cout << "두 개의 숫자입력:" << std::endl;
	std::cin >> num1 >> num2;

	try
	{
		if (num2 == 0)
		{
			throw num2;
		}
		std::cout << "나눗셈의 몫: " << num1 / num2 << std::endl;
		std::cout << "나눗셈의 나머지: " << num1 % num2 << std::endl;
	}
	catch(int expn)
	{
		std::cout << "제수는 " << expn << "이 될수없습니다." << std::endl;
		std::cout << "프로그램 다시 실행해라" << std::endl;
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