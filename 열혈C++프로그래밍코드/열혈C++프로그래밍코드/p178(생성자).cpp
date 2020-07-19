#include <iostream>

class Point
{
private:
	int x;
	int y;
public:
	//생성자가 명시되어 있지 않으면 default 생성자 알아서 만들어짐
	Point()
	{
		x = 0;
		y = 0;
	}
	//생성자 오버로딩
	Point(int x_)
	{
		x = x_;
		y = 0;
	}
	//생성자 오버로딩
	Point(int x_, int y_)
	{
		x = x_;
		y = y_;
	}
	//매개변수 default 값 설정 가능
	Point(int x_ = 0, int y_ = 0)
	{
		x = x_;
		y = y_;
	}
	//매개변수 default 값 설정할때 뒤에서 앞으로 설정해주어함, 앞에만 있고 뒤에만 있으면 컴파일에러
	Point(int x_, int y_=0)
	{
		x = x_;
		y = y_;
	}
};

class Rectangle
{
private:
	//oint & point;
	const int SIZE;
	//Point upLeft;
	//Point downRight;
public:
	//Rectangle(const int &x1, const int &y1, const int &x2, const int &y2, Point& other_point) :point(other_point),SIZE(10),upLeft(x1, y1), downRight(x2,y2)/*멤버변수를 생성과 동시에 초기화함*/
	//{
	//	//여기서 초기화해주면 선언한다음 초기화함
	//}
	Rectangle& CreateInitObj() const
	{
		Rectangle* rec = new Rectangle();
		return *rec;
	}
private:
	//private 생성자
	Rectangle() :SIZE(10) {}	
};

