#include <iostream>
#include <cstring>

template <typename T>
T Max(T a, t b)
{
	return a > b ? a : b;
}

template<>
//������ Max<char*>ó�� �ڷ��� ������ ����ϴ� ���� ����
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
	std::cout << Max("Simple", "Best"); //"Simple"�� ���ڿ� ����� const char*a �� ���ڷ� �ϴ� Maxȣ��
	char str1[] = "Simple";
	char str2[] = "Best";
	std::cout << Max(str1, str2);//char* a�� ���ڷ� �ϴ� Max�Լ� ȣ��
	

}