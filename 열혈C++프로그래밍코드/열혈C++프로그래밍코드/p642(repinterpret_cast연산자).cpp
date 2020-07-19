#include <iostream>

int main(void)
{
	int num = 0x010203;
	std::cout << &num << std::endl;
	//int포인터를 char형 포인터로 형 변환함
	char* ptr = reinterpret_cast<char*>(&num);

	for (int i = 0; i < sizeof(num); i++)
	{
		//char형 데이터를 int형으로 변환함
		std::cout << static_cast<int>(*(ptr + i)) << std::endl;
	}

	return 0;
}