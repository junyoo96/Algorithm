#include<iostream>
class Monster
{
public:
	int Attack(int a)
	{
		std::cout << "Attack";
		return 0;
	}

	//�Ű����� ����
	int Attack(int a, int b)
	{
		return 0;
	}

	//�Ű����� �ڷ���
	int Attack(float a, float b)
	{
		return 0;
	}

	//�Ű����� ����(�ڷ����� ����)
	int Attack(int a, float b)
	{
		return 0;
	}
	int Attack(float a, int b)
	{
		return 0;
	}

	//const���� ���� - const��ü�Ͻ� ȣ���, �Ϲݰ�ü�� �ٸ� �Լ� ȣ��
	int Attack(int a) const
	{
		std::cout << "const Attack";
		return 0;
	}

	//��ȯ���� �Լ��� �����ϴ� ������ �ƴ�
	/*float Attack(int a)
	{

	}*/
};

int main(void)
{
	Monster mon;
	int b=mon.Attack(3);
}