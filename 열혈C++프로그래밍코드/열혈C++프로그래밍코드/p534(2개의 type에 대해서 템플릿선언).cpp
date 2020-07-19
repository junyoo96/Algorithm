#include <iostream>

//��ǥ�� �̿��ؼ� 2�� �̻��� template type�� ����� �� ����
//typename��� class��� ����
template <class T1, class T2>
void ShowData(double num)
{	
	std::cout << (T1)num << ", " << (T2)num << std::endl;
}

int main(void)
{
	//�̷� ���ó�� ���޵Ǵ� ���ڸ� ���ؼ��� T1�� T2�� �ڷ����� �������� ����
	//����,���ø� �Լ��� ȣ�������� ������ ���缭 ȣ���ؾ���
	ShowData<char, int>(65);
	ShowData<short, double>(70.4);
	return 0;
}

