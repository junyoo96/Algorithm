//이름공간 std에 선언된 모든 것에 대해 이름공간 지정의 생략
using namespace std;
//이름공간 A에 속한 Defend를 호출할 때는 이름공간 지정할지 않고 호출하겠다는 의미를 전역으로 사용
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
//동일한 이름공간에 있는 함수면 호출할때 이름공간을 명시할 필요 없음
	Attack();
}

//이름공간 중첩
namespace C
{
	namespace D
	{
		void Attack();
	}
}

int main(void)
{
	//이름공간 A에 속한 Defend를 호출할 때는 이름공간 지정할지 않고 호출하겠다는 의미를 지역적으로 사용
	using A::Defend;
	//이름공간 별칭 지정
	namespace CD = C::D;
	
	//범위지정연산자를 이용한 지역변수에 가려진 전역변수 호출
	int a = 3;
	::a = 5;

	A::Attack();
	B::Attack();

	//중첩 접근
	C::D::Attack();
}