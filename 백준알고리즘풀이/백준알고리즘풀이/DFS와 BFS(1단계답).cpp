#include <iostream>
#include <queue>
#include <cstring> //memset
using namespace std;

const int MAX = 1000 + 1;

int N, M, V;
int adjacent[MAX][MAX]; //���� ���
bool visited[MAX]; //�湮�ߴ��� �ľ�
queue<int> q;

void DFS(int idx)
{
	cout << idx << " ";

	for (int i = 1; i <= N; i++)
		//�����ϰ� �湮���� �ʾҴٸ�
		if (adjacent[idx][i] && !visited[i])
		{
			visited[i] = true; //�湮�ߴٰ� ǥ��
							   //������ ��忡 ���ؼ� �� �ٽ� DFS
			DFS(i);
		}
}

void BFS(int idx)
{
	//ť�� idx�� �ְ� �湮�ߴٰ� ǥ��
	q.push(idx);
	visited[idx] = true;

	while (!q.empty())
	{
		idx = q.front();
		q.pop();

		cout << idx << " ";

		//BFS�� �ش� ��忡 ������ ������ ��� �߰��� �� BFS ����
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

	visited[V] = 1; //V���� �����ϹǷ�
	DFS(V);
	cout << "\n";

	//visited �迭�� �ʱ�ȭ
	memset(visited, false, sizeof(visited));
	BFS(V);
	cout << "\n";

	return 0;
}
