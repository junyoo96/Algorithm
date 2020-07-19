#include <iostream>

class Monster
{
private:
	int hp;
	char name[10];
public:
	Monster(const char* name_):hp(100)
	{
		strcpy_s(name, sizeof(name), name_);
	}	
	Monster* GetThisPointer()
	{
		//객체 자신을 가리키는 포인터 반환
		return this;
	}
	Monster& HpAdder(int hp)
	{
		this->hp += hp;
		//객체 자신을 참조할 수 있는 참조값 반환 
		return *this;
	}
	Monster& ShowHp()
	{
		//객체 자신을 참조할 수 있는 참조값 반환
		std::cout << hp << std::endl;
		std::cout << &hp << std::endl;
		return *this;
	}
};

int main(void)
{
	Monster mon("Zergling");
	//참조값을 이용해서 객체의 함수 연속해서 호출
	mon.HpAdder(10).ShowHp().HpAdder(20).ShowHp();
	return 0;
}
