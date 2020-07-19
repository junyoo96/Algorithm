#include <iostream>
#include <fstream>
#include <list>

void Solution(std::ifstream& ifstream)
{
	int num_person;
	int kill_turn;

	ifstream >> num_person >> kill_turn;

	std::list<int> survivors;
	for (int i = 1; i <= num_person; ++i)
	{
		survivors.push_back(i);
	}

	std::list<int>::iterator killer_pointer=survivors.begin();
	while (num_person > 2)
	{
		killer_pointer = survivors.erase(killer_pointer);
		--num_person;

		if (killer_pointer == survivors.end())
		{
			killer_pointer = survivors.begin();
		}

		int tmp = (kill_turn - 1) % num_person;
		for (int i = 0; i < tmp; ++i)
		{
			++killer_pointer;
			if (killer_pointer == survivors.end())
			{
				killer_pointer = survivors.begin();
			}
		}
	}

	std::cout << survivors.front() << " " << survivors.back() << std::endl;

}

int main(void)
{
	std::ifstream ifstream;
	ifstream.open("Input.txt");

	int test_case;
	ifstream >> test_case;

	for (int i = 0; i < test_case; ++i)
	{
		Solution(ifstream);
	}

	return 0;
}