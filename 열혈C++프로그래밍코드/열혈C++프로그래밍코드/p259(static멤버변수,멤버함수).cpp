#include <iostream>

class Apple
{
private:
	int size;
	//static ��� ����
	static int applecnt;
public:
	Apple() :size(10)
	{
		applecnt++;
		std::cout << applecnt << std::endl;
	}
	//static ��� �Լ�
	static void EatApple()
	{
		//static ��� ������ ���� ����
		applecnt--;
		std::cout << "remain: " << applecnt << std::endl;
		//static�Լ��� ��������� ���� ����
		//size = 0;
	}
};
//static��������� �ʱ�ȭ
int Apple::applecnt = 0;

class CountryArea
{
public:
	const static int RUSSIA = 100;
	const static int KOREA = 101;
};

int main(void)
{
	std::cout << CountryArea::RUSSIA << std::endl;
	std::cout << CountryArea::KOREA << std::endl;

	//Apple apple1;	
	//Apple apple2;
	////static����Լ��� public���� ����� ��� ���ٹ�� 
	//Apple::EatApple();
	
	return 0;
}