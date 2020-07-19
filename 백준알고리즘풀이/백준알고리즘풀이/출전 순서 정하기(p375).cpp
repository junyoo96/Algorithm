#include <iostream>
#include <fstream>
#include <vector>
#include <set>

int order(const std::vector<int>& russian, const std::vector<int>& korean)
{
	int n = russian.size();
	//���ڷ� �Ѿ range�� elements�� multiset ����
	std::multiset<int> korean_multiset(korean.begin(),korean.end());
	int wins=0;
	
	std::multiset<int>::iterator iter;

	for (int i = 0; i < n; ++i)
	{
		//korea������ ���� ���� ������ ���� russian������ �������� ���� ���
		if (*korean_multiset.rbegin() < russian[i])
		{
			korean_multiset.erase(korean_multiset.begin());
		}
		//korean������ �Ѹ��̶� ���� russian������ �������� ���� ���
		else
		{
			//russian������ �������� �������� korean������ ������ ���� ó�� ������ ������ russian������ �����̶��
			if (*korean_multiset.lower_bound(russian[i]) == russian[i])
			{
				std::multiset<int>::iterator iter_tmp = korean_multiset.lower_bound(russian[i]);
				//������ �ƴ� ������ ���� ���� ���� korean������ ��
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