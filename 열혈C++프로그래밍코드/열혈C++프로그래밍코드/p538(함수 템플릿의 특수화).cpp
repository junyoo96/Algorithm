#include <iostream>
#include <cstring>

template <typename T>
T Max(T a, t b)
{
	return a > b ? a : b;
}

template<>
//가급적 Max<char*>처럼 자료형 정보를 명시하는 것이 좋음
char* Max<char*>(char* a, char* b)
{
	return strlen(a) > strlen(b) ? a : b;
}

template<>
const char* Max<const char*>(const char*a, const char* b)
{
	return strcmp(a, b) > 0 ? a : b;
}

int main(void)
{	
	std::cout << Max("Simple", "Best"); //"Simple"은 문자열 상수라 const char*a 를 인자로 하는 Max호출
	char str1[] = "Simple";
	char str2[] = "Best";
	std::cout << Max(str1, str2);//char* a를 인자로 하는 Max함수 호출
	

}