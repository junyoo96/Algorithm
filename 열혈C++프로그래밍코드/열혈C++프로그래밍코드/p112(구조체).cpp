#include <iostream>

//���õ� ����� �ۿ��� namespace�� ����� �����ϰ� �� ������
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

	//�̷��� �ȿ��� enum�����Ҽ��� ����
	enum
	{
		MAX_HP = 30,
		MAX_SIZE = 300
	};

	int hp;
	int size;

	//C++������ ����ü �ȿ� �Լ� ���� ����
	void Heal();
	//����ü �ȿ� �Լ��� ���ǵǾ� ������ �Լ��� inline���� ó����
	//���� ���� �ϰ� �ۿ��� �����ϰ� �Ǹ� inline���� ó���ȵ�
	//inline�Լ��� �״�� �����ϰ� �ʹٸ� �ܺ� ���ǿ��� inline�Լ��� �����ϸ��
	void SizeUp();
};

//�Լ��� �ܺο��� ����
void Monster::Heal()
{
	if (hp + 10 <= MONSTER_CONST::MAX_HP)
	{
		hp += 10;
	}
	std::cout << "���� ü��: " <<hp<< std::endl;
}

//inline�Լ���� ���
inline void Monster::SizeUp()
{
	if (size + 100 <= MONSTER_CONST::MAX_SIZE)
	{
		size += 100;
	}
	std::cout << "���� size: " << size << std::endl;
}

int main(void)
{
	//����ü ���� �ʱ�ȭ
	Monster mon = { 10,100 };
	mon.Heal();
	mon.SizeUp();
}
