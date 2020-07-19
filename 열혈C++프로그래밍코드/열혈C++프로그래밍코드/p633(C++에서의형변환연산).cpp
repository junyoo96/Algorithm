#include <iostream>

class Car
{
private:
	int fuelGuage=100;
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
	/*포인터 변수 car1이 가리키는 대상이 실제로는 Truck객체이기 때문에 다음 형변환 연산은
	문제가 되지 않을 수 있다.
	하지만, 기초 클래스의 포인터 형을 유도클래스의 포인터형으로 변환하는 것은 일반적인 경우의 형 변환이 아님(불필요한 형 변환이기 때문)
	따라서, 이 상황에서 이것이 프로그래머의 의도인지, 실수인지 알 방법이 없음*/
	Truck* truck1 = (Truck*)car1;
	truck1->ShowTruckState();

	
	Car* car2 = new Car();
	/*포인터 변수 car2가 가리키는 대상이 실제로는 Car객체이기 때문에 37행의 형 변환 연산은 문제가 된다.
	하지만, C스타일의 형 변환 연산자는 컴파일러로 하여금 이러한 것을 가능하게함*/
	//컴파일러는 이 문장을 보고 "맞는 형 변환 연산인지 아닌지는 모르겠고, 일단 형 변환을 진행함"
	Truck* truck2 = (Truck*)car2;
	/*이 문장의 실행결과는 예측이 불가능핟다
	일단, 포인터변수 truck2가 가리키는 대상은 Car객체이기 때문에 ShowTruckState함수의 호출은 논리적으로 맞지가 않으며, 특히 이 객체에는
	화물의 무게를 의미하는 멤버 freightweight가 존재하지않음*/
	truck2->ShowTruckState();

	//결론적으로 실행은 되지만, 포인터가 가리키는 Car객체에는 freightweight가 없기 때문에 이상한 값이 나옴 
	return 0;
}