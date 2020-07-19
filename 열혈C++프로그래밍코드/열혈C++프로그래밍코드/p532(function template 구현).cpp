#include <iostream>

//컴파일러에 의해서 만들어지는 템플릿 함수는 일반함수와 구분됨
template <typename T>
T Add(T num1, T num2)
{
	std::cout << "T Add(T num1, T num2)" << std::endl;
	return num1 + num2;
}

//동일한 기능을 하는데 일반함수가 정의되어있으면 템플릿 함수보다 우선시 되서 호출, 일반함수가 없다면 템플릿 함수 호출됨
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
	//밑에 두개 함수는 일반 함수 호출됨
	std::cout << Add(5, 7) << std::endl;
	std::cout << Add(3.7, 7.5) << std::endl;
	//Add<int> 이렇게 명시해주면 일반함수말고 템플릿 함수 호출됨
	std::cout << Add<int>(5, 7) << std::endl;
	std::cout << Add<double>(3.7, 7.5) << std::endl;
}