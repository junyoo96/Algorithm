#include <iostream>

class First
{
public:
	First()
	{
		std::cout << "First积己" << std::endl;
	}
	virtual ~First()
	{
		std::cout << "First家戈" << std::endl;
	}
	virtual void SimpleFunc()
	{
		std::cout << "First狼 SimpleFunc()" << std::endl;
	}
};

class Second : public First
{
public:
	Second()
	{
		std::cout << "Second积己" << std::endl;
	}
	~Second()
	{
		std::cout << "Second家戈" << std::endl;
	}
	void SimpleFunc()
	{
		std::cout << "Second狼 SimpleFunc()" << std::endl;
	}
};

int main()
{
	/*First *fptr = new Second();
	delete fptr;*/

	Second obj;
	obj.SimpleFunc();

	First &fref = obj;
	fref.SimpleFunc();

}