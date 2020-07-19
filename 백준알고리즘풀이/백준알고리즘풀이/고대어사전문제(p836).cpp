//위상정렬 문제입니다.dfs를 사용하면 제일 앞에있는 정점이 제일 늦게 종료 된다는 개념을 이용해서
//
//reverse함수를 사용해 뒤집어주면 고대어 단어 사전 정렬이 문제에 알맞게 정렬됩니다.
//
//adj[a][b]가 존재할때 adj[b][a]가 존재한다는 것은 단어의 우선순위에 모순이 있기 때문에
//
//이 경우에만 빈 벡터를 반환해서
//
//INVALID HYPOTHESIS를 출력해주시면 됩니다.

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

#define TEST

std::ifstream ifStream;

//알파벳의 각 글자에 대하 인접행렬 표현
std::vector<std::vector<int>> adj_matrix_graph;
//주어진 단어들로부터 알파벳 간의 선후관계 그래프 생성
void MakeGraph(const std::vector<std::string>& _words)
{
	adj_matrix_graph = std::vector<std::vector<int>>(26, std::vector<int>(26, 0));
	for (int j = 1; j < _words.size(); ++j)
	{
		int i = j - 1;
		int len = std::min(_words[i].size(), _words[j].size());
		//word[i]가 word[j]앞에 오는 이유를 찾음
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

//adj_matrix_graph에 주어진 그래프를 위상정렬한 결과를 반환
//그래프가 DAG가 아니라면 빈 벡터를 반환
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
	//만약 그래프가 DAG가 아니라면 정렬 결과에 역방향 간선이 있음
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
	//없는 경우라면 깊이 우선 탐색에서 얻은 순서 반환
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

