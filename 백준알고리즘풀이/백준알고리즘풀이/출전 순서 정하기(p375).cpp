#include <iostream>
#include <fstream>
#include <vector>
#include <set>

int order(const std::vector<int>& russian, const std::vector<int>& korean)
{
	int n = russian.size();
	//인자로 넘어간 range의 elements로 multiset 생성
	std::multiset<int> korean_multiset(korean.begin(),korean.end());
	int wins=0;
	
	std::multiset<int>::iterator iter;

	for (int i = 0; i < n; ++i)
	{
		//korea팀원중 가장 높은 점수가 지금 russian팀원의 점수보다 작은 경우
		if (*korean_multiset.rbegin() < russian[i])
		{
			korean_multiset.erase(korean_multiset.begin());
		}
		//korean팀원중 한명이라도 지금 russian팀원의 점수보다 높은 경우
		else
		{
			//russian팀원의 점수보다 작지않은 korean팀원의 점수중 가장 처음 팀원의 점수가 russian팀원가 동점이라면
			if (*korean_multiset.lower_bound(russian[i]) == russian[i])
			{
				std::multiset<int>::iterator iter_tmp = korean_multiset.lower_bound(russian[i]);
				//동점이 아닐 때까지 점수 높은 다음 korean팀원을 고름
				do 
				{
					++iter_tmp;
				} while (*iter_tmp == russian[i]);

				korean_multiset.erase(iter_tmp);
				++wins;
			}
			else
			{
				korean_multiset.erase(korean_multiset.lower_bound(russian[i]));
				++wins;
			}
			
		}

		/*for (iter = korean_multiset.begin(); iter != korean_multiset.end(); ++iter)
		{
			std::cout << *iter << " ";
		}
		std::cout << "/" << russian[i] << std::endl;*/
		
	}

	return wins;

}

void Solution(std::ifstream& ifstream)
{
	std::vector<int> russian;
	russian.push_back(3000);
	russian.push_back(2700);
	russian.push_back(2800);
	russian.push_back(2200);
	russian.push_back(2500);
	russian.push_back(1900);

	std::vector<int> korean;
	korean.push_back(2800);
	korean.push_back(2750);
	korean.push_back(2995);
	korean.push_back(1800);
	korean.push_back(2600);
	korean.push_back(2000);

	std::cout<<order(russian, korean)<<std::endl;
}

int main(void)
{
	std::ifstream ifstream;
	ifstream.open("Input.txt");

	Solution(ifstream);
	return 0;
}