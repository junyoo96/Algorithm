#include <iostream>
#include <queue>
#include <vector>

std::vector<std::vector<int>> adj;

//1.BFS Spanning Tree 계산
void Bfs2(int start, std::vector<int>& distance, std::vector<int>& parent)
{
	distance = std::vector<int>(adj.size(), -1);
	parent = std::vector<int>(adj.size(), -1);

	//방문할 정점 목록을 유지하는 queue
	std::queue<int> q;
	distance[start] = 0;
	parent[start] = start;
	q.push(start);

	while (!q.empty())
	{
		int here = q.front();
		q.pop();
		
		//here정점에 인접한 다른정점들 검사 
		for (int i = 0; i < adj[here].size(); ++i)
		{
			int there = adj[here][i];
			//발견 안된 정점이라면
			if (distance[there] == -1)
			{
				q.push(there);
				//there정점의 거리 계산
				distance[there] = distance[here] + 1;
				//there정점의 부모정점 설정
				parent[there] = here;
			}
		}
	}
}

//2. Bfs Spanning Tree를 바탕으로 시작점과 임의의 정점 v까지의 최단 경로 계산 
std::vector<int> ShortestPath(int v, const std::vector<int>& parent)
{
	std::vector<int> path(1, v);
	while (parent[v] != v)
	{
		v = parent[v];
		path.push_back(v);
	}
	//정점에서 시작점까지의 순이기 때문에 reverse
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

	//1.BFS Spanning Tree 계산
	Bfs2(0, distance, parent);
	//2. Bfs Spanning Tree를 바탕으로 시작점과 임의의 정점 v까지의 최단 경로 계산 
	std::vector<int> path=ShortestPath(3, parent);

	for (int i = 0; i < path.size(); ++i)
	{
		std::cout << path[i] << std::endl;
	}
}



