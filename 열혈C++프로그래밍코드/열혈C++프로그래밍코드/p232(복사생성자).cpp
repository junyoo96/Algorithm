#include <iostream>

class Monster
{
private:
	int hp;
public:
	Monster(int hp_) :hp(hp_)
	{}
	//���������
	//��������ڸ� ������� ������ ����Ʈ ���� ������ �˾Ƽ� ������
	//�Ű������� constŰ���带 ������ ������ ���ѷ��� �ɸ�, �������� �� ������ 
	Monster(const Monster& copy) :hp(copy.hp)
	{
		std::cout << "��������� ȣ��" << std::endl;
	}
	~Monster()
	{
		std::cout << "�Ҹ��� ȣ��" << std::endl;
	}
};

Monster GetMonster(Monster mon)/*1. �Ű����� mon ��ü ���� - ���ڰ� ���޵ǰ� - mon�� ��������� ȣ��*/
{
	std::cout << "return ����" << std::endl;
	
	return mon;/*2. �ӽð�ü ����- mon��ü ���� - �ӽð�ü�� ��������� ȣ��*/
}

int main(void)
{
	//Monster mon1(100);
	////��������� ȣ�� - ���ο� ��ü ���� �� ���� ��ü�� �ʱ�ȭ
	//Monster mon2=mon1;
	//GetMonster(mon2);

	
	//std::cout << "after make!" << std::endl;

	////�ӽ� ��ü ������ ��ȯ�Ǵ� �������� mon�� ���޵Ǿ� mon�� �ӽð�ü�� ������
	//const Monster& mon = Monster(300);
	//std::cout << "after make!" << std::endl;


	Monster mon1(100);
	//�߰��� ��ü�� �������� �ʰ�, ��ȯ�Ǵ� �ӽð�ü�� mon2��� �̸��� �Ҵ���(��ü �������� �ϳ� �ٿ��� ȿ������ ���̱� ����)
	Monster mon2 = GetMonster(mon1);

	std::cout << "���α׷� ��" << std::endl;

	return 0;
}