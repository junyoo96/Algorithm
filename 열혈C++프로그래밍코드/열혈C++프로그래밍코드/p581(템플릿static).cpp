#include<iostream>

template<typename T>
class SimipleStaticMem
{
private:
	static T mem;
public:
	void AddMem(int num) { mem += num; }
	void ShowMem() { std::cout << mem << std::endl; }
};

//static member초기화
//template<typename T>는 그다음 문장이 template과 관련 있고 typename T를 기반으로하는 템플릿이라는 뜻
template<typename T>
T SimipleStaticMem<T>::mem = 0;
