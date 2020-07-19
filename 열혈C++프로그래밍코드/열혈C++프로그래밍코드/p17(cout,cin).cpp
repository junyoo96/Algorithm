#include <iostream>

int main(void)
{
	//1.입력
	//std::cout : 출력 명령
	//std::endl : 개행 명령
	// <<연산자를 이용함
	std::cout << "Hello World!" << std::endl;

	//2.출력
	int a = 0;
	//std::cin : 입력 명령
	//C++에서는 데이터의 입력도 데이터의 출력과 마찬가지로 별도의 포맷 지정이 필요없음(int형이든 char형이든)
	std::cin >> a;

	//3.배열기반의 입출력
	char name[100];
	std::cin >> name;
}