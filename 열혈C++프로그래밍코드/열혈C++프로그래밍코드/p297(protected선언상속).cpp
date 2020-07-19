#include <iostream>

//Base Class(기초 클래스)
class Monster
{
private:
	int hp;
	char name[50];
};

class Zergling : private Monster
{
private:
	char weapon[10];
};

//protected로 선언된 멤버변수는 이를 상속하는 유도 클래스에서 접근이 가능
class Zergling : protected Monster
{
private:
	char weapon[10];
};

class Zergling : public Monster
{
private:
	char weapon[10];
};



