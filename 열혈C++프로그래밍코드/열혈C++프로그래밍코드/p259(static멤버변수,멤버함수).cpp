#include <iostream>

class Apple
{
private:
	int size;
	//static 멤버 변수
	static int applecnt;
public:
	Apple() :size(10)
	{
		applecnt++;
		std::cout << applecnt << std::endl;
	}
	//static 멤버 함수
	static void EatApple()
	{
		//static 멤버 변수에 접근 가능
		applecnt--;
		std::cout << "remain: " << applecnt << std::endl;
		//static함수는 멤버변수에 접근 못함
		//size = 0;
	}
};
//static멤버변수의 초기화
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
	////static멤버함수가 public으로 선언된 경우 접근방식 
	//Apple::EatApple();
	
	return 0;
}