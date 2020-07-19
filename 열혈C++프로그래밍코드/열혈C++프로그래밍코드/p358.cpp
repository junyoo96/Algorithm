#include <iostream>

class First
{
public:
	First()
	{
		std::cout << "First����" << std::endl;
	}
	virtual ~First()
	{
		std::cout << "First�Ҹ�" << std::endl;
	}
	virtual void SimpleFunc()
	{
		std::cout << "First�� SimpleFunc()" << std::endl;
	}
};

class Second : public First
{
public:
	Second()
	{
		std::cout << "Second����" << std::endl;
	}
	~Second()
	{
		std::cout << "Second�Ҹ�" << std::endl;
	}
	void SimpleFunc()
	{
		std::cout << "Second�� SimpleFunc()" << std::endl;
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