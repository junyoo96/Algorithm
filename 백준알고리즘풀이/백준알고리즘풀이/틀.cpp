#include <iostream>
#include <fstream>
#define TEST

//���̵�� �ð� : 
//���� �ð� : 
//�� �ð� : 

std::fstream ifStream;

void Solution()
{

}

int main(void)
{
#ifdef TEST
	ifStream.open("Input.txt");
#endif
	Solution();

	return 0;
}
