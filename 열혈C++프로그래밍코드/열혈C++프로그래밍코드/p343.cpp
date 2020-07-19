#include<iostream>

class First
{
public:
	void FirstFunc()
	{
		std::cout << "FirstFunc()" << std::endl;
	}
};

class Second : public First 
{
public:
	void SecondFunc()
	{
		std::cout << "SecondFunc()" << std::endl;
	}
};

class Third : public Second
{
public:
	void ThirdFunc()
	{
		std::cout << "ThirdFunc()" << std::endl;
	}
};

int main(void)
{
	Third *tptr = new Third();
	Second *sptr = tptr;
	First *fptr = sptr;

	tptr->FirstFunc();
	tptr->SecondFunc();
	tptr->ThirdFunc();

	sptr->FirstFunc();
	sptr->SecondFunc();
	sptr->ThirdFunc(); //(x)

	fptr->FirstFunc();
	fptr->SecondFunc(); //(x)
	fptr->ThirdFunc();	//(x)
}
