#include <iostream>

int val1 = 10;

//���� num�� ���ȭ
const int num = 10;

//������ ptr1�� ���ؼ� val1�� ���� ������ �� ����
//�����Ͱ� ����Ű�� int�� �����͸� ������ �� ���ٰ� �����ϸ�ɵ�
const int* ptr1 = &val1;

//������ ptr2�� ���ȭ��
//ptr2�� ����� �ּҸ� const�����Ѵٰ� �����ϸ� �ɵ�
int* const ptr2 = &val1;
