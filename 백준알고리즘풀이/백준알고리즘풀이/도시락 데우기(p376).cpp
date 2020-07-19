#include <iostream>
#include <fstream>
#include <vector>'
#include <algorithm>

int Heat(int boxNum, std::vector<int>& eat, std::vector<int>& cook)
{
	std::vector<std::pair<int,int>> order;
	for (int i = 0; i < boxNum; ++i)
	{
		//�Դµ� �ɸ��� �ð��� ������������ ���ϰ� �����ϱ� ���� ���̳ʽ� �ٿ���
		//�̷��� ���� ū ���� ���� �������� �ǰ� �������� �������� �� ���� ���� ū���� �� �տ���
		order.push_back(std::make_pair(-eat[i],i));
	}
	std::sort(order.begin(), order.end());	

	int eatAndCookTimeSum = 0; 
	int beginEat = 0;
	for (int i = 0; i < boxNum; ++i)
	{
		int box = order[i].second;
		
		beginEat += cook[box];		
		//max(�� ���ö����� �� �Դµ� �ɸ��� �ð�, ���ݵ��ö��� �丮�ϰ� �Դµ� ���� �ɸ��� �ð�) ��
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