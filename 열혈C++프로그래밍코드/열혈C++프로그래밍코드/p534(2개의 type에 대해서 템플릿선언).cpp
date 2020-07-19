#include <iostream>

//쉼표를 이용해서 2개 이상의 template type을 명시할 수 있음
//typename대신 class사용 가능
template <class T1, class T2>
void ShowData(double num)
{	
	std::cout << (T1)num << ", " << (T2)num << std::endl;
}

int main(void)
{
	//이런 경우처럼 전달되는 인자를 통해서는 T1과 T2의 자료형을 결정짓지 못함
	//따라서,템플릿 함수의 호출형식을 완전히 갖춰서 호출해야함
	ShowData<char, int>(65);
	ShowData<short, double>(70.4);
	return 0;
}

