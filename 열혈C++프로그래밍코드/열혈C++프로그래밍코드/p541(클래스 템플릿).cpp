#include <iostream>

template <typename T>
class Point
{
private:
	T xpos, ypos;
public :
	Point(T x = 0, T y = 0) : xpos(x), ypos(y)
	{}
	void ShowPosition() const
	{
		std::cout << "xpos : " << xpos << " ypos: " << ypos << std::endl;
	}

	T SeparateFunction();
};

//Ŭ���� ���ø��� ����� ������ �и�
// Point<T>�� T�� ���� templateȭ�� PointŬ���� ���ø��� �ǹ�
template<typename T>
T Point<T>::SeparateFunction()
{
	T a;
	return a;
}

int main(void)
{
	//Point<int> ó�� Ŭ���� ���ø� ����� ��ü�������� �ݵ�� �ڷ��� ������ ����ϵ��� �Ǿ�����
	//�����Ϸ� ���忡�� ��ð� �ȵǾ������� � ���ø� Ŭ������ ���������� �𸣱� ����
	Point<int> pos1(3, 4);
	pos1.ShowPosition();

	Point<char> pos3('P', 'F');
	pos3.ShowPosition();
	return 0;
}