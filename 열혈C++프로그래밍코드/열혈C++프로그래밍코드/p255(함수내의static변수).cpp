#include <iostream>

void Counter()
{
	//static변수는 전역변수와 마찬가지로 초기화하지 않으면 0으로 초기화됨
	static int cnt=0;
	cnt++;
	std::cout << cnt << std::endl;
}

int main(void)
{
	for (int i = 0; i < 5; ++i)
	{
		Counter();
	}
	return 0;
}