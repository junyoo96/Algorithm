#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//걸린 시간 - 11:30

std::fstream ifStream;

int Conference()
{
	int n;
	std::vector<std::pair<int, int>> vec;	
	int answer=0;
#ifdef TEST
	ifStream >> n;
#else
	std::cin >> n;
#endif
	
	for (int i = 0; i < n; ++i)
	{
		int start;
		int end;
#ifdef TEST
		ifStream >> start >> end;
#else
		std::cin >> start >> end;
#endif
		//끝나는 시간 순
		vec.push_back(std::make_pair(end, start));
	}

	std::sort(vec.begin(), vec.end());

	int begin=0;
	for (int i = 0; i < n; ++i)
	{
		if (vec[i].second >= begin)
		{
			begin = vec[i].first;
			++answer;
		}
	}

	return answer;
}

void Solution()
{
	std::cout << Conference() << std::endl;
}

int main(void)
{
#ifdef TEST
	ifStream.open("Input.txt");
#endif
	Solution();

	return 0;
}
