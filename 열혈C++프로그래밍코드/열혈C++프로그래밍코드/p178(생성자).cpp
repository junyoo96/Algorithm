#include <iostream>

class Point
{
private:
	int x;
	int y;
public:
	//�����ڰ� ��õǾ� ���� ������ default ������ �˾Ƽ� �������
	Point()
	{
		x = 0;
		y = 0;
	}
	//������ �����ε�
	Point(int x_)
	{
		x = x_;
		y = 0;
	}
	//������ �����ε�
	Point(int x_, int y_)
	{
		x = x_;
		y = y_;
	}
	//�Ű����� default �� ���� ����
	Point(int x_ = 0, int y_ = 0)
	{
		x = x_;
		y = y_;
	}
	//�Ű����� default �� �����Ҷ� �ڿ��� ������ �������־���, �տ��� �ְ� �ڿ��� ������ �����Ͽ���
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
	//Rectangle(const int &x1, const int &y1, const int &x2, const int &y2, Point& other_point) :point(other_point),SIZE(10),upLeft(x1, y1), downRight(x2,y2)/*��������� ������ ���ÿ� �ʱ�ȭ��*/
	//{
	//	//���⼭ �ʱ�ȭ���ָ� �����Ѵ��� �ʱ�ȭ��
	//}
	Rectangle& CreateInitObj() const
	{
		Rectangle* rec = new Rectangle();
		return *rec;
	}
private:
	//private ������
	Rectangle() :SIZE(10) {}	
};

