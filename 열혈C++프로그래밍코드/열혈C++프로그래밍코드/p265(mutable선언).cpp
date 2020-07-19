#include <iostream>

class Apple
{
private:
	int size;
	//mutable 선언
	mutable bool isRotten;
public:
	Apple() : size(10), isRotten(false) 
	{}
	void MakeAppleRotten() const
	{		
		//const함수임에도 멤버변수 데이터 변경 가능
		isRotten = true;
		//일반 멤버변수는 변경 불가능
		size = 0;
	}
};

int main(void)
{
	Apple apple1;
	apple1.MakeAppleRotten();
	return 0;
}