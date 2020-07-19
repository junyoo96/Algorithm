#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
//#define TEST

//2020.01.17

//���̵�� �ð� : 8:03~8:32 
//���� �ð� : 8:41~
//�� �ð� : 

std::fstream ifStream;

double Line()
{
	int n;
	std::vector<std::pair<double, double>> lineList;

	double start;
	double end;

	double answer = 0;

#ifdef TEST
	ifStream >> n;
#else
	std::cin >> n;
#endif

	for (int i = 0; i < n; ++i)
	{
#ifdef TEST		
		ifStream >> start >> end;
#else
		std::cin >> start >> end;
#endif
		lineList.emplace_back(std::make_pair(start, end));
	}

	std::sort(lineList.begin(), lineList.end());

	start = -1000000000;
	end= -1000000000;

	for (int i = 0; i < lineList.size(); ++i)
	{
		double tmpStart=lineList[i].first;
		double tmpEnd = lineList[i].second;
		
		if (start <= tmpStart && tmpEnd <= end)
		{
			continue;
		}
		
		answer += tmpEnd - tmpStart;

		if (tmpStart < end)
		{
			answer -= (end - tmpStart);
		}
		start = tmpStart;
		end = tmpEnd;
	}


	return answer;
}

void Solution()
{
	std::cout << Line() << std::endl;
}

int main(void)
{
#ifdef TEST
	ifStream.open("Input.txt");
#endif
	Solution();

	return 0;
}
