#include <iostream>
#include <fstream>
#include <vector>
//#define TEST

//½Ã°£ : 22ºÐ

std::fstream ifStream;

int Coin()
{	
	std::vector<int> vec;
	int coinType;
	int valueSum;
	int count = 0;
#ifdef TEST
	input_stream >> coinType;
	input_stream >> valueSum;	
#else
	std::cin >> coinType;
	std::cin >> valueSum;
#endif


	for (int i = 0; i < coinType; ++i)
	{
		int tmp;
#ifdef TEST
		input_stream >> tmp;
#else
		std::cin >> tmp;
#endif
		vec.push_back(tmp);	
	}

	for (int i = coinType - 1; i >= 0; --i)
	{
		if (valueSum == 0)
		{
			return count;
		}

		if (valueSum >= vec[i])
		{
			count += valueSum / vec[i];
			valueSum %= vec[i];
		}
	}

	return count;
}

void Solution()
{	
	std::cout << Coin() << std::endl;
}

int main(void)
{
#ifdef TEST
	input_stream.open("Input.txt");
#endif
	Solution();

	return 0;
}
