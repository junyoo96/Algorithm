#include <iostream>

class Monster
{
private:
	char* name;
public:
	Monster(const char* name_)
	{
		//���� �Ҵ�
		name = new char[strlen(name_)+1];
		strcpy_s(name, strlen(name_) + 1, name_);
	}
	//�Ҹ���
	~Monster()
	{
		//�����ڿ��� ���� �Ҵ��Ѱ� ����
		delete []name;
	}
};

int main(void)
{
	Monster("Zergling");
	return 0;
}
