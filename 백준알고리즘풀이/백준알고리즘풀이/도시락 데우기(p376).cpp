#include <iostream>
#include <fstream>
#include <vector>'
#include <algorithm>

int Heat(int boxNum, std::vector<int>& eat, std::vector<int>& cook)
{
	std::vector<std::pair<int,int>> order;
	for (int i = 0; i < boxNum; ++i)
	{
		//먹는데 걸리는 시간을 내림차순으로 편하게 정렬하기 위해 마이너스 붙여줌
		//이러면 가장 큰 수가 가장 작은수가 되고 오름차순 정렬했을 때 원래 가장 큰수가 맨 앞에옴
		order.push_back(std::make_pair(-eat[i],i));
	}
	std::sort(order.begin(), order.end());	

	int eatAndCookTimeSum = 0; 
	int beginEat = 0;
	for (int i = 0; i < boxNum; ++i)
	{
		int box = order[i].second;
		
		beginEat += cook[box];		
		//max(전 도시락까지 다 먹는데 걸리는 시간, 지금도시락을 요리하고 먹는데 까지 걸리는 시간) 비교
		eatAndCookTimeSum = std::max(eatAndCookTimeSum, beginEat + eat[box]);		
	}
	
	return eatAndCookTimeSum;
}

void Solution(std::ifstream& ifstream)
{
	int testcases=0;
	
	ifstream >> testcases;	
	
	for (int i = 0; i < testcases; ++i)
	{		
		int boxNum;
		ifstream >> boxNum;		

		std::vector<int> eat;
		std::vector<int> cook;
		for (int i = 0; i < boxNum; ++i)
		{			
			int tmp;
			ifstream >> tmp;			
			cook.push_back(tmp);
		}
		
		for (int i = 0; i < boxNum; ++i)
		{
			int tmp;
			ifstream >> tmp;			
			eat.push_back(tmp);
		}

		std::cout<<Heat(boxNum, eat, cook) << std::endl;
		
	}

}

int main(void)
{
	std::ifstream ifstream;
	ifstream.open("Input.txt");

	Solution(ifstream);
	return 0;
}