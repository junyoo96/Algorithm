#include <iostream>
#include <vector>
#include <queue>

//�׷����� ��������Ʈ ǥ��
std::vector<std::vector<int>> adj;

std::vector<int> Bfs(int start)
{
	//���� �߰��ߴ��� ����
	std::vector<bool> discovered(adj.size(), false);
	//�湮�� ������ ����
	std::queue<int> q;
	//�湮�� ����
	std::vector<int> order;
	
	q.push(start);
	discovered[start] = true;
	
	while (!q.empty())
	{
		int here = q.front();
		q.pop();
		order.push_back(here);

		for (int i = 0; i < adj[here].size(); ++i)
		{
			int there = adj[here][i];
			if (!discovered[there])
			{
				q.push(there);
				discovered[there] = true;
			}
		}
	}

	return order;
}