#include<iostream>

class Boy;

class Girl
{
private:
	char phNum[20];
public:
	Girl(const char* num)
	{
		strcpy_s(phNum, sizeof(phNum), num);
	}
	void MakeBoyHeightUp(Boy& boy);

};

class Boy
{
private:
	int height;
public:
	Boy(int len) :height(len)
	{}
	//Girl클래스의 멤버함수에 대한 friend선언
	friend void Girl::MakeBoyHeightUp(Boy& boy);
	//전역함수에 대한 friend선언
	friend void ShowBoyInfo(const Boy& boy);
};

void Girl::MakeBoyHeightUp(Boy& boy)
{	
	boy.height += 10;
}


int main(void)
{
	Girl girl("010-1111");
	Boy boy(180);
	girl.MakeBoyHeightUp(boy);
	ShowBoyInfo(boy);
}

void ShowBoyInfo(const Boy& boy)
{
	std::cout << boy.height << std::endl;
}