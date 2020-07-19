#include<iostream>

//template 인자로 숫자를 전달해서 상수처럼 사용가능
template <typename T, int len>
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
	//이런식으로 인자가 다르면 서로 다른 자료형
	SimpleArray<int, 5> i5arr;
	SimpleArray<int, 7> i7arr;
	//따라서, 대입 불가
	i5arr = i7arr;
}