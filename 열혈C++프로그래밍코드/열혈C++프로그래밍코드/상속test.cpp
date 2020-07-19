#include<iostream>

class Monster
{
public:
	virtual void Attack()
	{
		std::cout << "Monster" << std::endl;
	}
};

class Digimon : public Monster
{
public:
	void Attack()
	{
		std::cout << "Digimon" << std::endl;
	}	
};

int main(void)
{
	Digimon digimon;
	Monster mon = digimon;
	mon.Attack();

	/*Monster* mon = new Digimon;
	mon->Attack();*/
}