#include <iostream>

class Car
{
private:
	int fuelGuage=100;
public:
	void ShowCarState()
	{
		std::cout << "ShowCarState�Լ�" << std::endl;
	}
};

class Truck : public Car
{
	int freighweight = 1000;
public:
	void ShowTruckState()
	{
		std::cout << "ShowTruckState�Լ�" << std::endl;
		std::cout << "ȭ���ǹ���" << freighweight << std::endl;
	}
};

int main(void)
{
	Car* car1 = new Truck();
	/*������ ���� car1�� ����Ű�� ����� �����δ� Truck��ü�̱� ������ ���� ����ȯ ������
	������ ���� ���� �� �ִ�.
	������, ���� Ŭ������ ������ ���� ����Ŭ������ ������������ ��ȯ�ϴ� ���� �Ϲ����� ����� �� ��ȯ�� �ƴ�(���ʿ��� �� ��ȯ�̱� ����)
	����, �� ��Ȳ���� �̰��� ���α׷����� �ǵ�����, �Ǽ����� �� ����� ����*/
	Truck* truck1 = (Truck*)car1;
	truck1->ShowTruckState();

	
	Car* car2 = new Car();
	/*������ ���� car2�� ����Ű�� ����� �����δ� Car��ü�̱� ������ 37���� �� ��ȯ ������ ������ �ȴ�.
	������, C��Ÿ���� �� ��ȯ �����ڴ� �����Ϸ��� �Ͽ��� �̷��� ���� �����ϰ���*/
	//�����Ϸ��� �� ������ ���� "�´� �� ��ȯ �������� �ƴ����� �𸣰ڰ�, �ϴ� �� ��ȯ�� ������"
	Truck* truck2 = (Truck*)car2;
	/*�� ������ �������� ������ �Ұ�������
	�ϴ�, �����ͺ��� truck2�� ����Ű�� ����� Car��ü�̱� ������ ShowTruckState�Լ��� ȣ���� �������� ������ ������, Ư�� �� ��ü����
	ȭ���� ���Ը� �ǹ��ϴ� ��� freightweight�� ������������*/
	truck2->ShowTruckState();

	//��������� ������ ������, �����Ͱ� ����Ű�� Car��ü���� freightweight�� ���� ������ �̻��� ���� ���� 
	return 0;
}