#include <iostream>
#include <queue>
#include <cstring> //memset
using namespace std;

const int MAX = 1000 + 1;

int N, M, V;
int adjacent[MAX][MAX]; //인접 행렬
bool visited[MAX]; //방문했는지 파악
queue<int> q;

void DFS(int idx)
{
	cout << idx << " ";

	for (int i = 1; i <= N; i++)
		//인접하고 방문하지 않았다면
		if (adjacent[idx][i] && !visited[i])
		{
			visited[i] = true; //방문했다고 표시
							   //인접한 노드에 대해서 또 다시 DFS
			DFS(i);
		}
}

void BFS(int idx)
{
	//큐에 idx를 넣고 방문했다고 표시
	q.push(idx);
	visited[idx] = true;

	while (!q.empty())
	{
		idx = q.front();
		q.pop();

		cout << idx << " ";

		//BFS는 해당 노드에 인접한 노드들을 모두 추가한 뒤 BFS 진행
		for (int i = 1; i <= N; i++)
			if (adjacent[idx][i] && !visited[i])
			{
				visited[i] = true;
				q.push(i);
			}
	}
}

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M >> V;

	for (int i = 0; i < M; i++)
	{
		int from, to;
		cin >> from >> to;
		adjacent[from][to] = 1;
		adjacent[to][from] = 1;
	}

	visited[V] = 1; //V에서 시작하므로
	DFS(V);
	cout << "\n";

	//visited 배열을 초기화
	memset(visited, false, sizeof(visited));
	BFS(V);
	cout << "\n";

	return 0;
}
