class Person
{

};

class Student : public Person
{

};

int main(void)
{
	Person* person = new Student();	
}