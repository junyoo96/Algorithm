#include<iostream>
#include<string>
#include<set>
#include<vector>
#include <algorithm>

int calcualateDn(int n);

int main(void)
{

	
	//생성자가 있는 숫자 저장하는 리스트
	std::set<int> generate_number_exist_list;
	//셀프넘버 저장하는 리스트
	std::vector<int> self_number_list;
	for (int i = 1; i <= 10000; ++i)
	{
		self_number_list.push_back(i);
	}
	
	//생성자가 없는 숫자 저장하는 리스트
	int n = 1;
	int dn;	

	//1.생성자 있는 숫자들 리스트에 저장
	//셀프넘버가 10000이 안넘을때까지 돌림
	while (n<=10000)
	{
		dn = calcualateDn(n);
		generate_number_exist_list.insert(dn);
		n++;
	}

	//std::cout << "debug4" << std::endl;

	////2.생성자에 없는 숫자들 
	std::set<int>::iterator iter;			

	int start = 0;
	for (iter = generate_number_exist_list.begin(); iter != generate_number_exist_list.end(); iter++)
	{
		int target_number=*iter;		
		for (int i = start; i < self_number_list.size(); ++i)
		{
			if (self_number_list[i]==target_number)
			{				
				start = i;
				self_number_list.erase(std::remove(self_number_list.begin(),self_number_list.end(),target_number),self_number_list.end());
				break;
			}
		}		
	}	

	//3.셀프넘버 출력
	for (int i = 0; i < self_number_list.size(); ++i)
	{
		std::cout << self_number_list[i] << std::endl;
	}

}

//d(n)을 계산하는 함수
int calcualateDn(int n)
{
	int result = n;

	int remain=0;
	while (n != 0)
	{
		remain += n % 10;
		n /= 10;
	}

	result += remain;
	return result;
}