#include<iostream>

//Attack함수내에서 참조자 ref를 이용하 값의 변경을 하지 않겠다는 의미
void Attack(const int& ref)
{

}

//반환형이 참조형인 함수
int& Func(int& ref)
{
	ref++;
	return ref;
}

//반환형이 기본자료형인 함수
int Func2(int& ref)
{
	ref++;
	return ref;
}

//주소값 이용(포인터)
void Copy(int* a_, int* b_)
{
	int temp = *a_;
}

//참조자 이용
void Copy(int& a_, int& b_)
{
	int temp = a_;
}


int main(void)
{
	int a = 3;
	////반환형이 참조형인 함수
	int num1 = Func(a); //반환값을 저장할 변수의 자료형이 기본자료형이면 값 저장
	int& numReference = Func(a); //반환값을 저장할 변수의 자료형이 참조자면 참조값 저장

	//반환형이 기본자료형인 함수
	int num1 = Func2(a); //반환값을 저장할 변수의 자료형이 기본자료형이면 값 저장
	int& numReference = Func2(a); //반환값을 저장할 변수의 자료형이 참조자면 오류(반환형이 int라 상수가 반환되기때문)

	

}

