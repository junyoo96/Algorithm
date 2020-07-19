#include <iostream>

class SoSimple
{
public:
	//�����Լ�
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
	//����Ŭ������ ����Ŭ������ ����ȯ
	SoComplex* comPtr = dynamic_cast<SoComplex*>(simPtr);
	comPtr->ShowSimpleInfo();
}