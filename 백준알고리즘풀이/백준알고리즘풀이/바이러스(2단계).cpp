#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//6:20~

std::fstream ifStream;
//�������� ����Ʈ
std::vector<std::vector<int>> adjacent_matrix;
//�湮���� ���
std::vector<bool> visited;
//�湮�� ��ǻ�� �� 
int count=0;

void Dfs(int start_point)
{
	visited[start_point] = true;
	//std::cout <<"visited : "<< start_point << std::endl;
	count++;

	for (int i = 0; i < adjacent_matrix[start_point].size(); ++i)
	{
		int tmp = adjacent_matrix[start_point][i];
		if (visited[tmp] == false)
		{
			Dfs(adjacent_matrix[start_point][i]);
		}		
	}

}

void DfsAll(int start_point)
{
	visited[start_point] = true;

	for (int i = 0; i < adjacent_matrix[start_point].size(); ++i)
	{
		int tmp = adjacent_matrix[start_point][i];
		if (visited[tmp] == false)
		{
			Dfs(tmp);
		}		
	}
}

void Solution()
{
	int num_com;
	int num_connected_com;	

#ifdef TEST
	input_stream >> num_com;
	input_stream >> num_connected_com;
#else
	std::cin >> num_com;
	std::cin >> num_connected_com;
#endif

	adjacent_matrix = std::vector<std::vector<int>>(num_com+1);
	visited = std::vector<bool>(adjacent_matrix.size(), false);

	//1.�������� ����Ʈ ����
	for (int i = 0; i < num_connected_com; ++i)
	{
		int from;
		int to;
#ifdef TEST
		input_stream >> from;
		input_stream >> to;
#else
		std::cin >> from;
		std::cin >> to;
#endif
		adjacent_matrix[from].push_back(to);
		adjacent_matrix[to].push_back(from);
	}

	//2.�������� ����Ʈ ����
	for (int i = 1; i < adjacent_matrix.size(); ++i)
	{
		std::sort(adjacent_matrix[i].begin(), adjacent_matrix[i].end());
	}

	//3.DFS����
	int start_point=1;
	DfsAll(start_point);

	//4.�湮�� ��ǻ�� �� ���
	std::cout << count << std::endl;

}

int main(void)
{
#ifdef TEST
	input_stream.open("Input.txt");
#endif
	Solution();

	return 0;
}
