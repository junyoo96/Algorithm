#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

//가능한 최대 회의 수 계산
int Schedule()
{
	int n;
	int begin[100];
	int end[100];

	//1. 회의 추가 및 끝나는 시간으로 오름차순 정렬
	std::vector<std::pair<int, int>> order;
	for (int i = 0; i < n; ++i)
	{
		order.push_back(std::make_pair(end[i], begin[i]));
	}
	//회의가 끝나는 시간으로 오름차순 정렬
	std::sort(order.begin(), order.end());

	//2.끝나는 시간에 맞춰서 가능한 최대 회의 수 계산
	//현시점 회의가 시작할 수 있는 가장 빠른 시간
	int earliest = 0; 
	//가능한 회의 수
	int selected = 0;

	for (int i = 0; i < order.size(); ++i)
	{
		int meeting_begin = order[i].second;
		int meeting_end = order[i].first;
		//현재의 회의가 지금 order에 들어간 회의의 마지막 시간 이후라면
		if (earliest <= meeting_begin)
		{
			earliest = meeting_end;
			++selected;
		}
	}
	
	return selected;
}

void Solution(std::ifstream& ifstream)
{
	Schedule();
}

int main(void)
{
	std::ifstream ifstream;
	ifstream.open("Input.txt");

	Solution(ifstream);
	return 0;
}