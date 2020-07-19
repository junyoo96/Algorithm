#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#define TEST

//���̵�� �ð� : 
//���� �ð� : 
//�� �ð� : 

//std::fstream ifStream;

void Solution()
{
	int cases;
	//ifStream >> cases;
	std::cin >> cases;

	//������ ���� ����
	std::vector<std::vector<int>> doublearray(cases,std::vector<int>(3,0));
	//����
	std::vector<std::vector<int>> doublearrayCopy(cases, std::vector<int>(3, 0));

	//������ �ޱ�
	for (int i = 0; i < cases; ++i)
	{
		for (int j = 0; j < 3; ++j)
		{
			int tmp;
			//ifStream >> tmp;
			std::cin >> tmp;
			doublearray[i][j] = tmp;
		}
	}

	//0��° �� ���� ���� �ϳ��� ��������  ����� ���� ������ �� ���� max��  �־��ٶ����
	int max = 1000 * cases - +1;

	//�ּ� �� ����(��)
	int min = 10000000;

	for (int i = 0; i < 3; ++i)
	{
		//�� ���� �ٲ� ������ �� ������ �迭 �ʱ�ȭ 
		for (int x = 0; x < cases; ++x)
		{
			for (int y = 0; y < cases; ++y)
			{
				doublearrayCopy[x][y] = doublearray[x][y];
			}
		}

		//0��° �� ���� ���� �ϳ��� ��������  ����� ���� ������ �� ���� max��  �־���
		for (int j = 0; j < cases; ++j)
		{
			if (j != i)
			{
				doublearrayCopy[0][j] = max;
			}			
		}		

		//�� ��� ���ϴ� ����
		for (int m = 1; m < cases; ++m)
		{
			doublearrayCopy[m][0] += std::min(doublearrayCopy[m - 1][1], doublearrayCopy[m - 1][2]);
			doublearrayCopy[m][1] += std::min(doublearrayCopy[m - 1][0], doublearrayCopy[m - 1][2]);
			doublearrayCopy[m][2] += std::min(doublearrayCopy[m - 1][0], doublearrayCopy[m - 1][1]);
		}

		//�� ����ϰ� ������ ���� �� ���� ����� ���� ������ �ϰ� ���ݱ��� ��� ������ �ϰ� ��
		for (int z = 0; z < 3; ++z)
		{
			
			if (doublearrayCopy[cases-1][z] < min && i!=z)
			{
				min = doublearrayCopy[cases - 1][z];
			}
		}
	}

	

	std::cout << min << std::endl;
	
	
}

int main(void)
{
//#ifdef TEST
//	ifStream.open("Input.txt");
//#endif
	Solution();

	return 0;
}
