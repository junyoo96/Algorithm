#include <iostream>

void Counter()
{
	//static������ ���������� ���������� �ʱ�ȭ���� ������ 0���� �ʱ�ȭ��
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