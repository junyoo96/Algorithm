#include <iostream>

class SoSimple
{
public:
	//가상함수
	virtual void ShowSimpleInfo()
	{
		std::cout << "SoSimple Base class" << std::endl;
	}
};

class SoComplex : public SoSimple
{
public:
	void ShowSimpleInfo()
	{
		std::cout << "SoComplex Derived Clas" << std::endl;
	}
};

int main(void)
{
	SoSimple* simPtr = new SoComplex;
	//기초클래스를 유도클래스로 형변환
	SoComplex* comPtr = dynamic_cast<SoComplex*>(simPtr);
	comPtr->ShowSimpleInfo();
}