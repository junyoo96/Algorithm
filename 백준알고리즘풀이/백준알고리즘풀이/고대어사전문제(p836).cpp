//�������� �����Դϴ�.dfs�� ����ϸ� ���� �տ��ִ� ������ ���� �ʰ� ���� �ȴٴ� ������ �̿��ؼ�
//
//reverse�Լ��� ����� �������ָ� ���� �ܾ� ���� ������ ������ �˸°� ���ĵ˴ϴ�.
//
//adj[a][b]�� �����Ҷ� adj[b][a]�� �����Ѵٴ� ���� �ܾ��� �켱������ ����� �ֱ� ������
//
//�� ��쿡�� �� ���͸� ��ȯ�ؼ�
//
//INVALID HYPOTHESIS�� ������ֽø� �˴ϴ�.

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

#define TEST

std::ifstream ifStream;

//���ĺ��� �� ���ڿ� ���� ������� ǥ��
std::vector<std::vector<int>> adj_matrix_graph;
//�־��� �ܾ��κ��� ���ĺ� ���� ���İ��� �׷��� ����
void MakeGraph(const std::vector<std::string>& _words)
{
	adj_matrix_graph = std::vector<std::vector<int>>(26, std::vector<int>(26, 0));
	for (int j = 1; j < _words.size(); ++j)
	{
		int i = j - 1;
		int len = std::min(_words[i].size(), _words[j].size());
		//word[i]�� word[j]�տ� ���� ������ ã��
		for (int k = 0; k < len; ++k)
		{
			if (_words[i][k] != _words[j][k])
			{
				int a = _words[i][k] - 'a';
				int b = _words[j][k] - 'a';
				adj_matrix_graph[a][b] = 1;

				break;
			}			
		}

	}
}

std::vector<int> visited, order;
void Dfs(int _here)
{
	visited[_here] = 1;
	for (int there = 0; there < adj_matrix_graph.size(); ++there)
	{
		if (adj_matrix_graph[_here][there] && !visited[there])
		{
			std::cout << char(_here+'a') << " " << (char)(there+'a') << std::endl;
			Dfs(there);
		}
	}
	order.push_back(_here);
}

//adj_matrix_graph�� �־��� �׷����� ���������� ����� ��ȯ
//�׷����� DAG�� �ƴ϶�� �� ���͸� ��ȯ
std::vector<int> TopologicalSort()
{
	int m = adj_matrix_graph.size();
	visited = std::vector<int>(m, 0);
	order.clear();
	for (int i = 0; i < m; ++i)
	{
		if (!visited[i])
		{
			Dfs(i);
		}			
	}
	reverse(order.begin(), order.end());
	//���� �׷����� DAG�� �ƴ϶�� ���� ����� ������ ������ ����
	for (int i = 0; i < m; ++i)
	{
		for (int j = i + 1; j < m; ++j)
		{
			std::cout << adj_matrix_graph[order[j]][order[i]] << " ";
			if (adj_matrix_graph[order[j]][order[i]])
			{				
				
				//return std::vector<int>();
			}
		}
		std::cout << std::endl;
	}
	//���� ����� ���� �켱 Ž������ ���� ���� ��ȯ
	return order;
}

void Solution()
{
	int num_words;
	std::vector<std::string> words_list;
	ifStream >> num_words;

	for (int i = 0; i < num_words; ++i)
	{
		std::string word;
		ifStream >> word;
		words_list.push_back(word);
	}
	
	MakeGraph(words_list);

	std::vector<int> answer=TopologicalSort();
	if (answer.empty( ))
	{
		std::cout << "INVALID HYPOTHESIS" << std::endl;
	}
	else
	{
		for (int i = 0; i < answer.size(); ++i)
		{

			std::cout << (char)( answer[i]+'a') << std::endl;
		}
	}	
}

int main(void)
{
	int testcase;
	ifStream.open("Input.txt");
	ifStream >> testcase;

	for (int i = 0; i < testcase; ++i)
	{
		Solution();
	}
}

