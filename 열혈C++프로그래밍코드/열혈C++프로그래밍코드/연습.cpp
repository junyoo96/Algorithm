#include <iostream>

class Person
{
public:
	Person()
	{
		std::cout << "person持失切" << std::endl;
	}
	~Person()
	{
		std::cout << "person社瑚切" << std::endl;
	}
};

class Man : public Person
{
public:
	Man()
	{
		std::cout << "man 持失切" << std::endl;
	}
	~Man()
	{
		std::cout << "man 社瑚切" << std::endl;
	}
};

int main(void)
{
	Man man;
	return 0;
}