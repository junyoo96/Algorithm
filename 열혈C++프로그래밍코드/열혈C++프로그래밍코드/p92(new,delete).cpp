int main(void)
{
	//메모리 동적 할당
	int* ptr1 = new int;
	double* ptr2 = new double;
	int* arr1 = new int[3];
	double* arr2 = new double[7];

	//메모리 할당 해제
	delete ptr1;
	delete ptr2;
	delete []arr1; //배열 할당 해제할 때
	delete[]arr2;
}