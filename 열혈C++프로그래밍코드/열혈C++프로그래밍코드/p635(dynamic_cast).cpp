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
	//���� Ŭ������ ���� Ŭ������ ��ȯ�Ϸ��� �ϸ� �����Ͽ����� ��
	Car* car1 = new Truck();	
	Truck* truck1 = dynamic_cast<Truck*>(car1);

	Car* car2 = new Car();
	Truck* truck2 = dynamic_cast<Truck*>(car2);

	//���� Ŭ������ ���� Ŭ������ ��ȯ�Ϸ��� �ϸ� ������
	Truck* truck3 = new Truck();
	Car* car3 = dynamic_cast<Car*>(truck3);


	return 0;
}