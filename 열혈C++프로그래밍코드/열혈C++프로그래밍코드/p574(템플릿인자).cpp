#include<iostream>

//template ���ڷ� ���ڸ� �����ؼ� ���ó�� ��밡��
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
	//�̷������� ���ڰ� �ٸ��� ���� �ٸ� �ڷ���
	SimpleArray<int, 5> i5arr;
	SimpleArray<int, 7> i7arr;
	//����, ���� �Ұ�
	i5arr = i7arr;
}