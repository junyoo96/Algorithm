#include <iostream>

class Monster
{
private:
	char* name;
public:
	Monster(const char* name_)
	{
		//동적 할당
		name = new char[strlen(name_)+1];
		strcpy_s(name, strlen(name_) + 1, name_);
	}
	//소멸자
	~Monster()
	{
		//생성자에서 동적 할당한거 해제
		delete []name;
	}
};

int main(void)
{
	Monster("Zergling");
	return 0;
}
