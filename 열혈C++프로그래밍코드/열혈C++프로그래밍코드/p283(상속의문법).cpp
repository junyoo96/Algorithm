#include <iostream>

//Base Class(기초 클래스)
class Monster
{
private:
	int hp;
	char name[50];
public:	
	Monster(int hp_,const char* name_): hp(hp_)
	{
		std::cout << "Monster 생성자" << std::endl;
		strcpy_s(name,sizeof(name),name_);
	}
	void GetMonsterHP() const
	{
		std::cout << "HP : " <<hp<< std::endl;
	}
	void GetMonsterName() const
	{
		std::cout << "NAME : " << name << std::endl;
	}
	~Monster()
	{
		std::cout << "Monster 소멸자" << std::endl;
	}
};

//Derived Class(유도 클래스)
class Zergling : public Monster
{
private:
	char weapon[10];
public:
	//Derived class에서는 Base class의 초기화에 대한 책임이 있음
	//따라서, Base class인 Monster의 인자까지 받음
	
	Zergling(int hp_, const char* name_, const char* weapon_) : Monster(hp_,name_)/*Initializer로 Base class의 생성자 호출(만약, Base class의 
																				  생성자 호출을 명시하지 않으면, Base class의 void생성자가 호출됨
																				  (이런경우, Base class에 void생성자가 명시되어 있어야함(자동으로 안만들어줌)*/																				 
	{
		std::cout << "Zergling 생성자" << std::endl;
		strcpy_s(weapon,sizeof(weapon),weapon_);
	}
	void WhoAreYou() const
	{
		//상속받았기 때문에 Base Class의 함수 사용가능
		GetMonsterHP();
		GetMonsterName();
		std::cout << "My weapon is: " <<weapon<< std::endl;
	}
	~Zergling()
	{
		std::cout << "Zergling 소멸자" << std::endl;		
	}
};

int main(void)
{	
	Zergling zergling1(10, "Zergling1", "claw");
	zergling1.WhoAreYou();	
	return 0;
}

