#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#define TEST

//���̵�� �ð� : 1 : 30~ 1: 45
//���� �ð� : 1:45 ~ 2: 02
//�� �ð� : 32��

std::fstream ifStream;

int Rope()
{
	int n;
	std::vector<int> ropeList;
	int answer = 0;
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
		ropeList.push_back(tmp);
	}

	std::sort(ropeList.begin(), ropeList.end());

	int z = n;
	for (int i = 0; i <n; ++i)
	{		
		int tmp= ropeList[i] * z;
		if (tmp > answer)
		{
			answer = tmp;
		}
		--z;
	}

	return answer;
}

void Solution()
{
	std::cout << Rope() << std::endl;
}

int main(void)
{
#ifdef TEST
	ifStream.open("Input.txt");
#endif
	Solution();

	return 0;
}
