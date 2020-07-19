#include<iostream>

//�ؿ��� Girl�� Class���� �ν��ϰ� �ϱ� ���� ����
//�� ������ ���� �ʾƵ� �� - �ؿ� Boy���� Girl�� ���� friend������ �� �� Girl�� ���� ���ǵ� ���� ���ֱ� ������ 
class Girl;

class Boy
{
private:
	int height;
	//Girl Class�� ���� friend ����
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
	//Boy Class�� ���� friend ����
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