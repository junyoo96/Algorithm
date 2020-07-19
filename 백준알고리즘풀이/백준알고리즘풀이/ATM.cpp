#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//�ɸ��ð� - 22��

std::fstream ifStream;

int ATM()
{
	int n;
	std::vector<int> vec;
	int answer=0;	
	
#ifdef TEST
	ifStream >> n;
#else
	std::cin >> n;
#endif
	for (int i = 0; i < n; ++i)
	{
		int tmp;
#ifdef TEST
		ifStream >> tmp;
#else
		std::cin >> tmp;
#endif
		vec.push_back(tmp);
	}

	std::sort(vec.begin(), vec.end());

	for (int i = 0; i < n; ++i)
	{
		//�� ���ڸ��� ���� Ƚ�� ���� �ϴ°�
		//1 , 1+2 , 1+2+3 �̸�, 1x3 + 2x2 + 3x1 �̷���
		answer += (n - i)*vec[i];		
	}

	return answer;
}

void Solution()
{
	std::cout << ATM() << std::endl;
}

int main(void)
{
#ifdef TEST
	ifStream.open("Input.txt");
#endif
	Solution();

	return 0;
}
