#include <iostream>

int val1 = 10;

//변수 num을 상수화
const int num = 10;

//포인터 ptr1을 통해서 val1의 값을 변경할 수 없음
//포인터가 가리키는 int형 데이터를 변경할 수 없다고 이해하면될듯
const int* ptr1 = &val1;

//포인터 ptr2가 상수화됨
//ptr2에 저장된 주소를 const선언한다고 이해하면 될듯
int* const ptr2 = &val1;
