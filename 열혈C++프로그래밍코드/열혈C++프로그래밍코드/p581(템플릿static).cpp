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

//static member�ʱ�ȭ
//template<typename T>�� �״��� ������ template�� ���� �ְ� typename T�� ��������ϴ� ���ø��̶�� ��
template<typename T>
T SimipleStaticMem<T>::mem = 0;
