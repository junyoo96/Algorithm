#include <iostream>

//�����Ϸ��� ���ؼ� ��������� ���ø� �Լ��� �Ϲ��Լ��� ���е�
template <typename T>
T Add(T num1, T num2)
{
	std::cout << "T Add(T num1, T num2)" << std::endl;
	return num1 + num2;
}

//������ ����� �ϴµ� �Ϲ��Լ��� ���ǵǾ������� ���ø� �Լ����� �켱�� �Ǽ� ȣ��, �Ϲ��Լ��� ���ٸ� ���ø� �Լ� ȣ���
int Add(int num1, int num2)
{
	std::cout << "Add(int num1, int num2)" << std::endl;
	return num1 + num2;
}

double Add(double num1, double num2)
{
	std::cout << "Add(double num1,double num2)" << std::endl;
	return num1 + num2;
}

int main(void)
{	
	//�ؿ� �ΰ� �Լ��� �Ϲ� �Լ� ȣ���
	std::cout << Add(5, 7) << std::endl;
	std::cout << Add(3.7, 7.5) << std::endl;
	//Add<int> �̷��� ������ָ� �Ϲ��Լ����� ���ø� �Լ� ȣ���
	std::cout << Add<int>(5, 7) << std::endl;
	std::cout << Add<double>(3.7, 7.5) << std::endl;
}