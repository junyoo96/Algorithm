#include <iostream>
#include <queue>
#include <vector>

std::vector<std::vector<int>> adj;

//1.BFS Spanning Tree ���
void Bfs2(int start, std::vector<int>& distance, std::vector<int>& parent)
{
	distance = std::vector<int>(adj.size(), -1);
	parent = std::vector<int>(adj.size(), -1);

	//�湮�� ���� ����� �����ϴ� queue
	std::queue<int> q;
	distance[start] = 0;
	parent[start] = start;
	q.push(start);

	while (!q.empty())
	{
		int here = q.front();
		q.pop();
		
		//here������ ������ �ٸ������� �˻� 
		for (int i = 0; i < adj[here].size(); ++i)
		{
			int there = adj[here][i];
			//�߰� �ȵ� �����̶��
			if (distance[there] == -1)
			{
				q.push(there);
				//there������ �Ÿ� ���
				distance[there] = distance[here] + 1;
				//there������ �θ����� ����
				parent[there] = here;
			}
		}
	}
}

//2. Bfs Spanning Tree�� �������� �������� ������ ���� v������ �ִ� ��� ��� 
std::vector<int> ShortestPath(int v, const std::vector<int>& parent)
{
	std::vector<int> path(1, v);
	while (parent[v] != v)
	{
		v = parent[v];
		path.push_back(v);
	}
	//�������� ������������ ���̱� ������ reverse
	reverse(path.begin(), path.end());
	return path;
}

int main(void)
{
	adj = std::vector<std::vector<int>>(4);

	adj[0].push_back(1);
	adj[0].push_back(2);
	adj[0].push_back(3);
	adj[1].push_back(2);
	adj[1].push_back(3);
	adj[2].push_back(1);	
	adj[3].push_back(1);

	std::vector<int> distance;
	std::vector<int> parent;

	//1.BFS Spanning Tree ���
	Bfs2(0, distance, parent);
	//2. Bfs Spanning Tree�� �������� �������� ������ ���� v������ �ִ� ��� ��� 
	std::vector<int> path=ShortestPath(3, parent);

	for (int i = 0; i < path.size(); ++i)
	{
		std::cout << path[i] << std::endl;
	}
}



