#include<iostream>
#include<string>
#include<set>
#include<vector>
#include <algorithm>

int calcualateDn(int n);

int main(void)
{

	
	//�����ڰ� �ִ� ���� �����ϴ� ����Ʈ
	std::set<int> generate_number_exist_list;
	//�����ѹ� �����ϴ� ����Ʈ
	std::vector<int> self_number_list;
	for (int i = 1; i <= 10000; ++i)
	{
		self_number_list.push_back(i);
	}
	
	//�����ڰ� ���� ���� �����ϴ� ����Ʈ
	int n = 1;
	int dn;	

	//1.������ �ִ� ���ڵ� ����Ʈ�� ����
	//�����ѹ��� 10000�� �ȳ��������� ����
	while (n<=10000)
	{
		dn = calcualateDn(n);
		generate_number_exist_list.insert(dn);
		n++;
	}

	//std::cout << "debug4" << std::endl;

	////2.�����ڿ� ���� ���ڵ� 
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

	//3.�����ѹ� ���
	for (int i = 0; i < self_number_list.size(); ++i)
	{
		std::cout << self_number_list[i] << std::endl;
	}

}

//d(n)�� ����ϴ� �Լ�
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