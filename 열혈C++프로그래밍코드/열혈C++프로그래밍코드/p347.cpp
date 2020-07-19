#include<iostream>

class First
{
public:
	virtual void MyFunc() = 0;
	
		//std::cout << "FirstFunc()" << std::endl;
	
};

class Second : public First
{
public:
	virtual void MyFunc()
	{
		std::cout << "SecondFunc()" << std::endl;
	}
};

class Third : public Second
{
public:
	virtual void MyFunc()
	{
		std::cout << "ThirdFunc()" << std::endl;
	}
};

int main(void)
{
	Second *sptr = new Second();
	sptr->MyFunc();

	delete sptr;

	sptr = new Third();
	sptr->MyFunc();

	return 0;
}

