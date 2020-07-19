#include<iostream>
class Monster
{
public:
	int Attack(int a)
	{
		std::cout << "Attack";
		return 0;
	}

	//매개변수 개수
	int Attack(int a, int b)
	{
		return 0;
	}

	//매개변수 자료형
	int Attack(float a, float b)
	{
		return 0;
	}

	//매개변수 순서(자료형에 따른)
	int Attack(int a, float b)
	{
		return 0;
	}
	int Attack(float a, int b)
	{
		return 0;
	}

	//const선언 여부 - const객체일시 호출됨, 일반객체는 다른 함수 호출
	int Attack(int a) const
	{
		std::cout << "const Attack";
		return 0;
	}

	//반환형은 함수를 구분하는 기준이 아님
	/*float Attack(int a)
	{

	}*/
};

int main(void)
{
	Monster mon;
	int b=mon.Attack(3);
}