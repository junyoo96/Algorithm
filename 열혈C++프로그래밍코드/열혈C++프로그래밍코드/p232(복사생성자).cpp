#include <iostream>

class Monster
{
private:
	int hp;
public:
	Monster(int hp_) :hp(hp_)
	{}
	//복사생성자
	//복사생성자를 명시하지 않으면 디폴트 복사 생성자 알아서 생성됨
	//매개변수에 const키워드를 붙이지 않으면 무한루프 걸림, 컴파일할 때 오류뜸 
	Monster(const Monster& copy) :hp(copy.hp)
	{
		std::cout << "복사생성자 호출" << std::endl;
	}
	~Monster()
	{
		std::cout << "소멸자 호출" << std::endl;
	}
};

Monster GetMonster(Monster mon)/*1. 매개변수 mon 객체 생성 - 인자가 전달되고 - mon의 복사생성자 호출*/
{
	std::cout << "return 이전" << std::endl;
	
	return mon;/*2. 임시객체 생성- mon객체 전달 - 임시객체의 복사생성자 호출*/
}

int main(void)
{
	//Monster mon1(100);
	////복사생성자 호출 - 새로운 객체 생성 후 기존 객체로 초기화
	//Monster mon2=mon1;
	//GetMonster(mon2);

	
	//std::cout << "after make!" << std::endl;

	////임시 객체 생성시 반환되는 참조값이 mon에 전달되어 mon이 임시객체를 참조함
	//const Monster& mon = Monster(300);
	//std::cout << "after make!" << std::endl;


	Monster mon1(100);
	//추가로 객체를 생성하지 않고, 반환되는 임시객체에 mon2라는 이름을 할당함(객체 생성수를 하나 줄여서 효율성을 높이기 위해)
	Monster mon2 = GetMonster(mon1);

	std::cout << "프로그램 끝" << std::endl;

	return 0;
}