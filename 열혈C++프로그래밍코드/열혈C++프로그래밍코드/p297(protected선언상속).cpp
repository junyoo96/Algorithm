#include <iostream>

//Base Class(���� Ŭ����)
class Monster
{
private:
	int hp;
	char name[50];
};

class Zergling : private Monster
{
private:
	char weapon[10];
};

//protected�� ����� ��������� �̸� ����ϴ� ���� Ŭ�������� ������ ����
class Zergling : protected Monster
{
private:
	char weapon[10];
};

class Zergling : public Monster
{
private:
	char weapon[10];
};



