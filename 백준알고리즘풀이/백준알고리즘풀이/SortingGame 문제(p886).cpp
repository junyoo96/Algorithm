#include <iostream>
#include <vector>
#include <queue>
#include <map>

//��� ������ ���� �ʿ��� ������ ������ ���� ����
std::map<std::vector<int>, int> to_sort;

//1.[0, 1, 2.., n - 1]�� ��� ������ ���� �ʿ��� ������ ������ ���� ���
void precalc(int n)
{
	//������ ����ϱ� ���� ���ĵ� 0~n-1������ �ӽ� ����
	std::vector<int> perm(n);
	for (int i = 0; i < n; ++i)
	{
		perm[i] = i;
	}
	
	//�湮������ ������ ������ queue
	std::queue<std::vector<int>> q;
	q.push(perm);
	to_sort[perm] = 0;
	
	while (!q.empty())
	{
		std::vector<int> here = q.front();
		q.pop();
		
		int cost = to_sort[here];
		//������ ������鼭 �� �������� ������ ���� �������� ��� ������ ������ �����ؾ��ϴ��� ���
		for (int i = 0; i < n; ++i)
		{
			for (int j = i + 2; j <= n; ++j)
			{
				reverse(here.begin() + i, here.begin() + j);
				//������ ������ map�� ���ٸ�
				if (to_sort.count(here) == 0)
				{
					//������ ���� 1ȸ �߰��Ѵٴ� �ǹ�
					to_sort[here] = cost + 1;
					q.push(here);
				}
				//�������� ���� �������·� ����
				reverse(here.begin() + i, here.begin() + j);
			}
		}
	}
}

int solve(const std::vector<int>& perm)
{
	//perm : ���� �־��� ����
	int n = perm.size();
	//perm�� ������ ����� ��Ҹ� ǥ���ϴ� ���� 
	std::vector<int> fixed(n);
	for (int i = 0; i < n; ++i)
	{
		int bigger = 0;
		for (int j = 0; j < n; ++j)
		{
			//perm[i]�� �������� ��� ���ڵ麸�� �� ū�� ���
			if (perm[j] < perm[i])
			{
				++bigger;
			}
		}
		fixed[i] = bigger;
	}

	//�̹� ����� ���� n������ ������ ���� �ʿ��� ������ ������ ���� �̿��� 
	//perm�� �����ϴµ� �ʿ��� ������ ������ ���� ������ ���
	return to_sort[fixed];
}

//2.  �� ����� �̿��� perm(���� �־��� �迭)�� �����ϴµ� �ʿ��� ������ ������ ���� ���
int main(void)
{
	std::vector<int> perm2(3);

	perm2.push_back(1);
	perm2.push_back(0);
	perm2.push_back(2);

	//1. [0,1,2..,n-1]�� ��� ������ ���� �ʿ��� ������ ������ ���� ���
	precalc(3);

	//2.  �� ����� �̿��� perm(���� �־��� �迭)�� �����ϴµ� �ʿ��� ������ ������ ���� ���
	std::cout << solve(perm2);	
}
