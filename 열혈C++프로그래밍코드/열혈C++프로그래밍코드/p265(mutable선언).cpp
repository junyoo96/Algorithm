#include <iostream>

class Apple
{
private:
	int size;
	//mutable ����
	mutable bool isRotten;
public:
	Apple() : size(10), isRotten(false) 
	{}
	void MakeAppleRotten() const
	{		
		//const�Լ��ӿ��� ������� ������ ���� ����
		isRotten = true;
		//�Ϲ� ��������� ���� �Ұ���
		size = 0;
	}
};

int main(void)
{
	Apple apple1;
	apple1.MakeAppleRotten();
	return 0;
}