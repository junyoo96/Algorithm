#include<iostream>

//template 인자로 숫자를 전달해서 상수처럼 사용가능
template <typename T=int, int len=7>
class SimpleArray
{
private:
	T arr[len];
public:
	T & operator[] (int idx)
	{
		return arr[idx];
	}
	SimpleArray<T, len>& operator=(const SimpleArray<T, len>& ref)
	{
		for (int i = 0; i < len; i++)
		{
			arr[i] = ref.arr[i];
			return *this;
		}
	}
};

int main(void)
{
	SimpleArray<> arr;
	SimpleArray<int> arr2;
	//이렇게 첫번째 매개변수 생략하고 두번째 매개변수 넣어주는 것은 불가능!
	SimpleArray<5> arr3;
}