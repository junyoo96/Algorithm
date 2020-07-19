#include<iostream>

class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) :num(n)
	{
	}
	void SimpleFunc()
	{
		std::cout << "SimpleFunc : " << num << std::endl;
	}
	//�Լ��� const����
	void SimpleFunc() const
	{
		std::cout << "const SimpleFunc : " << num << std::endl;
	}
};


int main(void)
{
	SoSimple obj1(2);
	//��ü�� const ����( ��ü�� ������� ������ ������� �ʰڴٴ� �ǹ� ) - const ����Լ��� ȣ�⸸ ����ϰڴٴ� ��
	const SoSimple obj2(7);

	//const���� ������ �Լ� �����ε� ���ǿ� �ش��
	//const������ �ȵ� ��ü�� ��� ȣ��
	obj1.SimpleFunc();
	//const������ �� ��ü�� ��� ȣ��
	obj2.SimpleFunc();

	return 0;
}