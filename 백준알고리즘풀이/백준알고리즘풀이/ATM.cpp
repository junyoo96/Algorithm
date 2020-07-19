#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//걸린시간 - 22분

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
		//각 숫자마다 더한 횟수 갖고 하는거
		//1 , 1+2 , 1+2+3 이면, 1x3 + 2x2 + 3x1 이렇게
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
