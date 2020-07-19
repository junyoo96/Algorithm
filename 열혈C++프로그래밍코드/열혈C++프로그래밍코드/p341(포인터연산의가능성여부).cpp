class Base
{

};

class Derived : public Base
{

};

int main(void)
{
	Base *bptr = new Derived();
	// Derived *dptr = bptr; //(x)

	Derived *dptr2 = new Derived();
	Base *bptr2 = dptr2; // (0)

}