#include <iostream>

int main(void)
{
	//1.�Է�
	//std::cout : ��� ���
	//std::endl : ���� ���
	// <<�����ڸ� �̿���
	std::cout << "Hello World!" << std::endl;

	//2.���
	int a = 0;
	//std::cin : �Է� ���
	//C++������ �������� �Էµ� �������� ��°� ���������� ������ ���� ������ �ʿ����(int���̵� char���̵�)
	std::cin >> a;

	//3.�迭����� �����
	char name[100];
	std::cin >> name;
}