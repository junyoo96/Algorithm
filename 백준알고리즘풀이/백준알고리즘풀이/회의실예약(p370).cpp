#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

//������ �ִ� ȸ�� �� ���
int Schedule()
{
	int n;
	int begin[100];
	int end[100];

	//1. ȸ�� �߰� �� ������ �ð����� �������� ����
	std::vector<std::pair<int, int>> order;
	for (int i = 0; i < n; ++i)
	{
		order.push_back(std::make_pair(end[i], begin[i]));
	}
	//ȸ�ǰ� ������ �ð����� �������� ����
	std::sort(order.begin(), order.end());

	//2.������ �ð��� ���缭 ������ �ִ� ȸ�� �� ���
	//������ ȸ�ǰ� ������ �� �ִ� ���� ���� �ð�
	int earliest = 0; 
	//������ ȸ�� ��
	int selected = 0;

	for (int i = 0; i < order.size(); ++i)
	{
		int meeting_begin = order[i].second;
		int meeting_end = order[i].first;
		//������ ȸ�ǰ� ���� order�� �� ȸ���� ������ �ð� ���Ķ��
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