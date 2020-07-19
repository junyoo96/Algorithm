#include <iostream>
#include <vector>
#include <queue>
#include <map>

//모든 순열에 대해 필요한 뒤집기 연산의 수를 저장
std::map<std::vector<int>, int> to_sort;

//1.[0, 1, 2.., n - 1]의 모든 순열에 대해 필요한 뒤집기 연산의 수를 계산
void precalc(int n)
{
	//순열을 계산하기 위한 정렬된 0~n-1까지의 임시 순열
	std::vector<int> perm(n);
	for (int i = 0; i < n; ++i)
	{
		perm[i] = i;
	}
	
	//방문예정인 순열을 저장할 queue
	std::queue<std::vector<int>> q;
	q.push(perm);
	to_sort[perm] = 0;
	
	while (!q.empty())
	{
		std::vector<int> here = q.front();
		q.pop();
		
		int cost = to_sort[here];
		//순열을 뒤집어가면서 각 뒤집어진 순열이 원래 순열부터 몇번 뒤집는 연산을 수행해야하는지 계산
		for (int i = 0; i < n; ++i)
		{
			for (int j = i + 2; j <= n; ++j)
			{
				reverse(here.begin() + i, here.begin() + j);
				//뒤집은 순열이 map에 없다면
				if (to_sort.count(here) == 0)
				{
					//뒤집는 연산 1회 추가한다는 의미
					to_sort[here] = cost + 1;
					q.push(here);
				}
				//뒤집었던 순열 이전상태로 복구
				reverse(here.begin() + i, here.begin() + j);
			}
		}
	}
}

int solve(const std::vector<int>& perm)
{
	//perm : 원래 주어진 순열
	int n = perm.size();
	//perm의 숫자의 상대적 대소를 표시하는 순열 
	std::vector<int> fixed(n);
	for (int i = 0; i < n; ++i)
	{
		int bigger = 0;
		for (int j = 0; j < n; ++j)
		{
			//perm[i]를 기준으로 몇개의 숫자들보다 더 큰지 계산
			if (perm[j] < perm[i])
			{
				++bigger;
			}
		}
		fixed[i] = bigger;
	}

	//이미 계산해 놓은 n까지의 순열에 대해 필요한 뒤집기 연산의 수를 이용해 
	//perm을 정렬하는데 필요한 뒤집기 연산의 수를 간단히 계산
	return to_sort[fixed];
}

//2.  이 결과를 이용해 perm(원래 주어진 배열)을 정렬하는데 필요한 뒤집기 연산의 수를 계산
int main(void)
{
	std::vector<int> perm2(3);

	perm2.push_back(1);
	perm2.push_back(0);
	perm2.push_back(2);

	//1. [0,1,2..,n-1]의 모든 순열에 대해 필요한 뒤집기 연산의 수를 계산
	precalc(3);

	//2.  이 결과를 이용해 perm(원래 주어진 배열)을 정렬하는데 필요한 뒤집기 연산의 수를 계산
	std::cout << solve(perm2);	
}
