#include <iostream>

class Car
{
private:
	int fuelGuage = 100;
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

	Truck* truck1 = static_cast<Truck*>(car1);
	truck1->ShowTruckState();


	Car* car2 = new Car();
	
	Truck* truck2 = static_cast<Truck*>(car2);	
	truck2->ShowTruckState();

	//�������� �Ѵٵ����� �ι�° �Ŵ� ���� �̻��ϰ� ����
	//���������, static�����ڴ� dynamic_cast�����ڿ� �޸�, ���� ���� �� ��ȯ ���
	//������, �� ����� ���� ���α׷��Ӱ� å���� ���� �Ǽ� dynamic_cast�����ڸ� ����ؼ� �������� �������ϰ�
	//�������� ��Ȳ���� å������ ���� ���� static_cast �����ڸ� ����ؾ���

	//�⺻�ڷ��� �����Ͱ��� �� ��ȯ���� ��밡��
	double result = static_cast<double>(20) / 3;
	
	return 0;
}