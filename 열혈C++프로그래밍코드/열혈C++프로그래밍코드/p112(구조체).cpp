#include <iostream>

//관련된 상수를 밖에서 namespace를 사용해 접근하게 할 수있음
namespace MONSTER_CONST
{
	enum
	{
		MAX_HP = 30,
		MAX_SIZE=300
	};
}

struct Monster
{

	//이렇게 안에서 enum선언할수도 있음
	enum
	{
		MAX_HP = 30,
		MAX_SIZE = 300
	};

	int hp;
	int size;

	//C++에서는 구조체 안에 함수 삽입 가능
	void Heal();
	//구조체 안에 함수가 정의되어 있으면 함수를 inline으로 처리함
	//만약 선언만 하고 밖에서 정의하게 되면 inline으로 처리안됨
	//inline함수로 그대로 유지하고 싶다면 외부 정의에서 inline함수로 선언하면됨
	void SizeUp();
};

//함수를 외부에서 정의
void Monster::Heal()
{
	if (hp + 10 <= MONSTER_CONST::MAX_HP)
	{
		hp += 10;
	}
	std::cout << "현재 체력: " <<hp<< std::endl;
}

//inline함수라고 명시
inline void Monster::SizeUp()
{
	if (size + 100 <= MONSTER_CONST::MAX_SIZE)
	{
		size += 100;
	}
	std::cout << "현재 size: " << size << std::endl;
}

int main(void)
{
	//구조체 변수 초기화
	Monster mon = { 10,100 };
	mon.Heal();
	mon.SizeUp();
}
