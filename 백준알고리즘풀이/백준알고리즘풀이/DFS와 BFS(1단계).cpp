#include <iostream>
#include <vector>
#include <fstream>
#include <stack>
#include <queue>
#include <algorithm>

#define TEST
std::ifstream ifStream;


//stack���
void dfs(std::vector<std::vector<int>>& _graph, int _start_point, std::vector<int>& _visit)
{

	//1.�湮�߾����� Ȯ��
	if (_visit[_start_point])
	{
		return;
	}

	//2.�湮�������� �鷯�� �湮�ߴٰ� ǥ��
	std::cout << _start_point << " ";

	_visit[_start_point] = true;

	//3.���� �������� �̵�
	for (int i = 0; i < _graph[_start_point].size(); ++i)
	{
		dfs(_graph,_graph[_start_point][i],_visit);
	}

}

void bfs(std::vector<std::vector<int>>& _graph, int _start_point, std::vector<int>& _visit)
{
	std::queue<int> queue;	
	queue.push(_start_point);
	_visit[_start_point] = 1;

	while (!queue.empty())
	{
		int queue_top = queue.front();	

		std::cout << queue_top << " ";

		for (int i = 0; i < _graph[queue_top].size(); ++i)
		{
			//1.�湮�߾����� Ȯ��
			if (_visit[_graph[queue_top][i]])
			{
				continue; 
			}

			//2.�湮�������� �鷯�� �湮�ߴٰ� ǥ��			
			_visit[_graph[queue_top][i]] = 1;
			queue.push(_graph[queue_top][i]);		
			
		}		
		queue.pop();
	}
	
}

void SetGraph(std::vector<std::vector<int>>& _graph, int _num_lines)
{
	int vertice_one = 0;
	int vertice_two = 0;	

	for (int i = 0; i < _num_lines; ++i)
	{		
#ifdef TEST
		ifStream >> vertice_one;
		ifStream >> vertice_two;
#else
		std::cin >> vertice_one;
		std::cin >> vertice_two;
#endif	
		_graph[vertice_one].push_back(vertice_two);
		_graph[vertice_two].push_back(vertice_one);
	}
	
	//sort�ؾ� ����ũ���� Ž����
	for (int i = 1; i <= _num_lines; ++i)
	{
		std::sort(_graph[i].begin(), _graph[i].end());
	}

	/*for (int i = 1; i <= _num_lines; ++i)
	{
		for (int j = 0; j < _graph[i].size(); ++j)
		{
			std::cout << i << " ";
			std::cout << _graph[i][j] << " ";
			std::cout << std::endl;
		}
		
	}*/

}



int main(void)
{
	
	int num_vertices=0;
	int num_lines = 0;
	int start_point = 0;

#ifdef TEST
	ifStream.open("Input.txt");
	ifStream >> num_vertices;
	ifStream >> num_lines;
	ifStream >> start_point;
#else
	std::cin >> num_vertices;
	std::cin >> num_lines;
	std::cin >> start_point;
#endif
		
	//1.Graph����
	//vector�� index�� ���� index�� �����ֱ� ����
	std::vector<std::vector<int>> graph(num_vertices+1);
	SetGraph(graph, num_lines);

	//2.DFS����
	//�湮 Ȯ�� ����
	std::vector<int> visit(graph.size(), 0);
	dfs(graph, start_point,visit);	
	
	std::cout << std::endl;
	
	for (int i = 0; i < visit.size(); ++i)
	{
		visit[i] = 0;
	}

	//3.BFS����
	bfs(graph,start_point,visit);

	return 0;
}