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
		//��ü �ڽ��� ����Ű�� ������ ��ȯ
		return this;
	}
	Monster& HpAdder(int hp)
	{
		this->hp += hp;
		//��ü �ڽ��� ������ �� �ִ� ������ ��ȯ 
		return *this;
	}
	Monster& ShowHp()
	{
		//��ü �ڽ��� ������ �� �ִ� ������ ��ȯ
		std::cout << hp << std::endl;
		std::cout << &hp << std::endl;
		return *this;
	}
};

int main(void)
{
	Monster mon("Zergling");
	//�������� �̿��ؼ� ��ü�� �Լ� �����ؼ� ȣ��
	mon.HpAdder(10).ShowHp().HpAdder(20).ShowHp();
	return 0;
}
