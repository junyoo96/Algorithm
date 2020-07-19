#include<iostream>

//클래스 템플릿
template <typename T1, typename T2>
class MySimple
{
public:
	void WhoAreYou()
	{
		std::cout << "size of T1:" << sizeof(T1) << std::endl;
		std::cout << "size of T1:" << sizeof(T2) << std::endl;
		std::cout << "<typename  T1, typename T2>"<< std::endl;
	}
};

//클래스 템플릿의 특수화(템플릿 클래스-T를 사용하지 않고 이미 직접 명시해준 클래스)
template<>
class MySimple<int, double>
{
public:
	void WhoAreYou()
	{
		std::cout << "size of int: " << sizeof(int) << std::endl;
		std::cout << "size of double: " << sizeof(double) << std::endl;
		std::cout << "<int,doyble>" << std::endl;
	}
};

//클래스 템플릿의 부분특수화(클래스 템플릿- 부분적으로T를 상요해서 Class를 만드는 template역할함)
template<typename T1>
class MySimple<T1, double>
{
public:
	void WhoAreYou()
	{
		std::cout << "size of T1" << sizeof(T1) << std::endl;
		std::cout << "size of dobule" << sizeof(double) << std::endl;
		std::cout << "<T1,dobule>" << std::endl;
	}
};

int main(void)
{
	//부분특수화된 클래스 템플릿을 사용해 객체 생성	
	MySimple<char, double> obj1;
	obj1.WhoAreYou();
	//클래스 템플릿을 사용해 객체 생성
	MySimple<int, long> obj2;
	obj2.WhoAreYou();
	//특수화된 클래스 템플릿을 사용해 객체 생성
	MySimple<int, double> obj3;
	obj3.WhoAreYou();
	return 0;
}