#include<iostream>

//template ���ڷ� ���ڸ� �����ؼ� ���ó�� ��밡��
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
	//�̷��� ù��° �Ű����� �����ϰ� �ι�° �Ű����� �־��ִ� ���� �Ұ���!
	SimpleArray<5> arr3;
}