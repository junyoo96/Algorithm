#include<iostream>

//Attack�Լ������� ������ ref�� �̿��� ���� ������ ���� �ʰڴٴ� �ǹ�
void Attack(const int& ref)
{

}

//��ȯ���� �������� �Լ�
int& Func(int& ref)
{
	ref++;
	return ref;
}

//��ȯ���� �⺻�ڷ����� �Լ�
int Func2(int& ref)
{
	ref++;
	return ref;
}

//�ּҰ� �̿�(������)
void Copy(int* a_, int* b_)
{
	int temp = *a_;
}

//������ �̿�
void Copy(int& a_, int& b_)
{
	int temp = a_;
}


int main(void)
{
	int a = 3;
	////��ȯ���� �������� �Լ�
	int num1 = Func(a); //��ȯ���� ������ ������ �ڷ����� �⺻�ڷ����̸� �� ����
	int& numReference = Func(a); //��ȯ���� ������ ������ �ڷ����� �����ڸ� ������ ����

	//��ȯ���� �⺻�ڷ����� �Լ�
	int num1 = Func2(a); //��ȯ���� ������ ������ �ڷ����� �⺻�ڷ����̸� �� ����
	int& numReference = Func2(a); //��ȯ���� ������ ������ �ڷ����� �����ڸ� ����(��ȯ���� int�� ����� ��ȯ�Ǳ⶧��)

	

}

