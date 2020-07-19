#include <iostream>

//Base Class(���� Ŭ����)
class Monster
{
private:
	int hp;
	char name[50];
public:	
	Monster(int hp_,const char* name_): hp(hp_)
	{
		std::cout << "Monster ������" << std::endl;
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
		std::cout << "Monster �Ҹ���" << std::endl;
	}
};

//Derived Class(���� Ŭ����)
class Zergling : public Monster
{
private:
	char weapon[10];
public:
	//Derived class������ Base class�� �ʱ�ȭ�� ���� å���� ����
	//����, Base class�� Monster�� ���ڱ��� ����
	
	Zergling(int hp_, const char* name_, const char* weapon_) : Monster(hp_,name_)/*Initializer�� Base class�� ������ ȣ��(����, Base class�� 
																				  ������ ȣ���� ������� ������, Base class�� void�����ڰ� ȣ���
																				  (�̷����, Base class�� void�����ڰ� ��õǾ� �־����(�ڵ����� �ȸ������)*/																				 
	{
		std::cout << "Zergling ������" << std::endl;
		strcpy_s(weapon,sizeof(weapon),weapon_);
	}
	void WhoAreYou() const
	{
		//��ӹ޾ұ� ������ Base Class�� �Լ� ��밡��
		GetMonsterHP();
		GetMonsterName();
		std::cout << "My weapon is: " <<weapon<< std::endl;
	}
	~Zergling()
	{
		std::cout << "Zergling �Ҹ���" << std::endl;		
	}
};

int main(void)
{	
	Zergling zergling1(10, "Zergling1", "claw");
	zergling1.WhoAreYou();	
	return 0;
}

