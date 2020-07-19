#include<iostream>

//밑에서 Girl이 Class임을 인식하게 하기 위해 선언
//이 선언을 하지 않아도 됨 - 밑에 Boy에서 Girl에 대해 friend선언을 할 때 Girl에 대한 정의도 같이 해주기 때문에 
class Girl;

class Boy
{
private:
	int height;
	//Girl Class에 대한 friend 선언
	friend class Girl;
public:
	Boy(int len):height(len)
	{}	
	void ShowYourFriendInfo(Girl &frn);
};

class Girl
{
private : 
	char phNum[20];
public:
	Girl(const char* num)
	{
		strcpy_s(phNum,sizeof(phNum), num);
	}
	void ShowYourFriendInfo(Boy& frn);
	//Boy Class에 대한 friend 선언
	friend class Boy;
};

void Boy::ShowYourFriendInfo(Girl &frn)
{
	std::cout << "Her number"<<frn.phNum << std::endl;
}

void Girl::ShowYourFriendInfo(Boy& frn)
{
	std::cout <<"His height:"<< frn.height << std::endl;
}

int main(void)
{
	Boy boy(170);
	Girl girl("010-1234-5678");
	boy.ShowYourFriendInfo(girl);
	girl.ShowYourFriendInfo(boy);
}