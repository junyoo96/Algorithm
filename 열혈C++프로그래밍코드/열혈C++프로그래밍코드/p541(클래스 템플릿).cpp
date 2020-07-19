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

//클래스 템플릿의 선언과 정의의 분리
// Point<T>는 T에 대해 template화된 Point클래스 템플릿을 의미
template<typename T>
T Point<T>::SeparateFunction()
{
	T a;
	return a;
}

int main(void)
{
	//Point<int> 처럼 클래스 템플릿 기반의 객체생성에는 반드시 자료형 정보를 명시하도록 되어있음
	//컴파일러 입장에서 명시가 안되어있으면 어떤 템플릿 클래스를 만들어야할지 모르기 때문
	Point<int> pos1(3, 4);
	pos1.ShowPosition();

	Point<char> pos3('P', 'F');
	pos3.ShowPosition();
	return 0;
}