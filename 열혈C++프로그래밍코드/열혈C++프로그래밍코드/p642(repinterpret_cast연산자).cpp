#include <iostream>

int main(void)
{
	int num = 0x010203;
	std::cout << &num << std::endl;
	//int�����͸� char�� �����ͷ� �� ��ȯ��
	char* ptr = reinterpret_cast<char*>(&num);

	for (int i = 0; i < sizeof(num); i++)
	{
		//char�� �����͸� int������ ��ȯ��
		std::cout << static_cast<int>(*(ptr + i)) << std::endl;
	}

	return 0;
}