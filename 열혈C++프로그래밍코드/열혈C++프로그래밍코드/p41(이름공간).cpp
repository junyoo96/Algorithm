//�̸����� std�� ����� ��� �Ϳ� ���� �̸����� ������ ����
using namespace std;
//�̸����� A�� ���� Defend�� ȣ���� ���� �̸����� �������� �ʰ� ȣ���ϰڴٴ� �ǹ̸� �������� ���
using A::Defend;
int a;

namespace A
{
	void Attack();
	void Defend();
}

namespace B
{
	void Attack();
}

void A::Defend()
{
//������ �̸������� �ִ� �Լ��� ȣ���Ҷ� �̸������� ����� �ʿ� ����
	Attack();
}

//�̸����� ��ø
namespace C
{
	namespace D
	{
		void Attack();
	}
}

int main(void)
{
	//�̸����� A�� ���� Defend�� ȣ���� ���� �̸����� �������� �ʰ� ȣ���ϰڴٴ� �ǹ̸� ���������� ���
	using A::Defend;
	//�̸����� ��Ī ����
	namespace CD = C::D;
	
	//�������������ڸ� �̿��� ���������� ������ �������� ȣ��
	int a = 3;
	::a = 5;

	A::Attack();
	B::Attack();

	//��ø ����
	C::D::Attack();
}