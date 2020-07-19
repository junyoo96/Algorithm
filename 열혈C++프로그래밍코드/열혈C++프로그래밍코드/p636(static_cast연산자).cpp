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
	Car* car1 = new Truck();	

	Truck* truck1 = static_cast<Truck*>(car1);
	truck1->ShowTruckState();


	Car* car2 = new Car();
	
	Truck* truck2 = static_cast<Truck*>(car2);	
	truck2->ShowTruckState();

	//컴파일은 둘다되지만 두번째 거는 값이 이상하게 나옴
	//결론적으로, static연산자는 dynamic_cast연산자와 달리, 보다 많은 형 변환 허용
	//하지만, 그 결과에 대해 프로그래머가 책임을 져야 되서 dynamic_cast연산자를 사용해서 안전성을 높여야하고
	//예외적인 상황에서 책임질수 있을 때만 static_cast 연산자를 사용해야함

	//기본자료형 데이터간의 형 변환에도 사용가능
	double result = static_cast<double>(20) / 3;
	
	return 0;
}