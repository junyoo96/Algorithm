#include <iostream>

class Person
{
public:
	Person()
	{
		std::cout << "person������" << std::endl;
	}
	~Person()
	{
		std::cout << "person�Ҹ���" << std::endl;
	}
};

class Man : public Person
{
public:
	Man()
	{
		std::cout << "man ������" << std::endl;
	}
	~Man()
	{
		std::cout << "man �Ҹ���" << std::endl;
	}
};

int main(void)
{
	Man man;
	return 0;
}