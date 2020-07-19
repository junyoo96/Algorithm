#include <iostream>
#include <vector>
#include <queue>

//그래프의 인접리스트 표현
std::vector<std::vector<int>> adj;

std::vector<int> Bfs(int start)
{
	//정점 발견했는지 여부
	std::vector<bool> discovered(adj.size(), false);
	//방문할 예정인 정점
	std::queue<int> q;
	//방문한 순서
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