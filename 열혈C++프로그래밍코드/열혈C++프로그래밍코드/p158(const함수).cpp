#include<iostream>

class Zealot
{
public:
	int hp;
};

class Dragoon
{
private:
	int hp;
public:
	//const함수
	void Union(Zealot& zealot_) const
	{
		//동일 클래스의 멤버변수 값 변경 불가
		hp +=zealot_.hp;
		//다른 클래스의 멤버변수 값 변경 가능
		zealot_.hp = 0;		
	}
};