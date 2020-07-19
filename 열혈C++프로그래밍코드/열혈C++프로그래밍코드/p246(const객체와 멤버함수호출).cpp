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
	//함수의 const선언
	void SimpleFunc() const
	{
		std::cout << "const SimpleFunc : " << num << std::endl;
	}
};


int main(void)
{
	SoSimple obj1(2);
	//객체의 const 선언( 객체의 멤버변수 변경을 허용하지 않겠다는 의미 ) - const 멤버함수의 호출만 허용하겠다는 뜻
	const SoSimple obj2(7);

	//const선언 유무도 함수 오버로딩 조건에 해당됨
	//const선언이 안된 객체일 경우 호출
	obj1.SimpleFunc();
	//const선언이 된 객체일 경우 호출
	obj2.SimpleFunc();

	return 0;
}