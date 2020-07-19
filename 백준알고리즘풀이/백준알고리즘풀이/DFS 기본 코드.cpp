#include <iostream>
#include <vector>

//�׷����� ���� ����Ʈ ǥ��
std::vector<std::vector<int>> adj_list_graph;
//�� ���� �湮 ����
std::vector<bool> visited;

void dfs(int _start_vertice)
{
	std::cout << "DFS Visits " << _start_vertice << std::endl;
	visited[_start_vertice] = true;
	//��� ���� ������ ��ȸ
	for (int i = 0; i < adj_list_graph[_start_vertice].size(); ++i)
	{
		int there = adj_list_graph[_start_vertice][i];
		//���� �湮���ߴٸ� �湮
		if (!visited[there])
		{
			dfs(there);
		}
	}
}
void dfsAll()
{
	visited = std::vector<bool>(adj_list_graph.size(), false);
	//��� ���� ��ȸ�ϸ鼭, ���� �湮���� ������ �湮
	for (int i = 0; i < adj_list_graph.size(); ++i)
	{
		if (!visited[i])
		{
			dfs(i);
		}
	}
}
int main(void)
{
	int num_vertices = 5;
	adj_list_graph = std::vector<std::vector<int>>(num_vertices);
	adj_list_graph[0].push_back(1);
	adj_list_graph[0].push_back(2);
	adj_list_graph[1].push_back(3);
	adj_list_graph[1].push_back(4);
	adj_list_graph[2].push_back(0);
	adj_list_graph[3].push_back(1);
	adj_list_graph[4].push_back(1);
	dfsAll();
}
