int main(void)
{
	//�޸� ���� �Ҵ�
	int* ptr1 = new int;
	double* ptr2 = new double;
	int* arr1 = new int[3];
	double* arr2 = new double[7];

	//�޸� �Ҵ� ����
	delete ptr1;
	delete ptr2;
	delete []arr1; //�迭 �Ҵ� ������ ��
	delete[]arr2;
}