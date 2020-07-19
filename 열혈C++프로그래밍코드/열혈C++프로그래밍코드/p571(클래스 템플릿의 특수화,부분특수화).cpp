#include<iostream>

//Ŭ���� ���ø�
template <typename T1, typename T2>
class MySimple
{
public:
	void WhoAreYou()
	{
		std::cout << "size of T1:" << sizeof(T1) << std::endl;
		std::cout << "size of T1:" << sizeof(T2) << std::endl;
		std::cout << "<typename  T1, typename T2>"<< std::endl;
	}
};

//Ŭ���� ���ø��� Ư��ȭ(���ø� Ŭ����-T�� ������� �ʰ� �̹� ���� ������� Ŭ����)
template<>
class MySimple<int, double>
{
public:
	void WhoAreYou()
	{
		std::cout << "size of int: " << sizeof(int) << std::endl;
		std::cout << "size of double: " << sizeof(double) << std::endl;
		std::cout << "<int,doyble>" << std::endl;
	}
};

//Ŭ���� ���ø��� �κ�Ư��ȭ(Ŭ���� ���ø�- �κ�������T�� ����ؼ� Class�� ����� template������)
template<typename T1>
class MySimple<T1, double>
{
public:
	void WhoAreYou()
	{
		std::cout << "size of T1" << sizeof(T1) << std::endl;
		std::cout << "size of dobule" << sizeof(double) << std::endl;
		std::cout << "<T1,dobule>" << std::endl;
	}
};

int main(void)
{
	//�κ�Ư��ȭ�� Ŭ���� ���ø��� ����� ��ü ����	
	MySimple<char, double> obj1;
	obj1.WhoAreYou();
	//Ŭ���� ���ø��� ����� ��ü ����
	MySimple<int, long> obj2;
	obj2.WhoAreYou();
	//Ư��ȭ�� Ŭ���� ���ø��� ����� ��ü ����
	MySimple<int, double> obj3;
	obj3.WhoAreYou();
	return 0;
}