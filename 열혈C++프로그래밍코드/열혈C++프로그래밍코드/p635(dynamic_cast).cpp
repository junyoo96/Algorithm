#include <iostream>

class Car
{
private:
	int fuelGuage = 100;
public:
	void ShowCarState()
	{
		std::cout << "ShowCarState함수" << std::endl;
	}
};

class Truck : public Car
{
	int freighweight = 1000;
public:
	void ShowTruckState()
	{
		std::cout << "ShowTruckState함수" << std::endl;
		std::cout << "화물의무게" << freighweight << std::endl;
	}
};

int main(void)
{
	//기초 클래스를 유도 클래스로 변환하려고 하면 컴파일에러가 남
	Car* car1 = new Truck();	
	Truck* truck1 = dynamic_cast<Truck*>(car1);

	Car* car2 = new Car();
	Truck* truck2 = dynamic_cast<Truck*>(car2);

	//유도 클래스를 기초 클래스로 변환하려고 하면 괜찮음
	Truck* truck3 = new Truck();
	Car* car3 = dynamic_cast<Car*>(truck3);


	return 0;
}