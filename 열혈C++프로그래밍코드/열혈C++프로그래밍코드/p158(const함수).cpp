#include<iostream>

class Zealot
{
public:
	int hp;
};

class Dragoon
{
private:
	int hp;
public:
	//const�Լ�
	void Union(Zealot& zealot_) const
	{
		//���� Ŭ������ ������� �� ���� �Ұ�
		hp +=zealot_.hp;
		//�ٸ� Ŭ������ ������� �� ���� ����
		zealot_.hp = 0;		
	}
};