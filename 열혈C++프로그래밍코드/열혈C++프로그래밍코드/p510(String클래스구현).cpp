#include<string>
#include<iostream>
//#define _CRT_SECURE_NO_WARNINGS

class String
{
private:
	int len;
	char* str;
public:
	String();
	String(const char* s);
	String(const String& s);
	~String();
	String& operator=(const String& s);
	String& operator+=(const String& s);
	bool operator==(const String& s);
	String operator+(const String& s);


	friend std::ostream& operator<< (std:: ostream& os, const String& s);
	friend std::istream& operator>> (std::istream& is, String& s);
};

String::String()
{
	len = 0;
	str = NULL;
}

String::String(const char* s)
{
	//std::cout << "String char ������" << std::endl;
	//null���� �ϳ��� �� ��
	len = strlen(s) + 1;
	str = new char[len];
	//*	
	//���� ����
	//std::cout << sizeof(str) << "/"<<sizeof(s) << std::endl;
	//sizeof��� len�� ���ִ� ������ sizeof(str)�� �����ͺ����� byte��
	//�����ؼ� ��ȯ�ϱ� ������ len���� byte�� �Ҵ���
	strcpy_s(str,len, s);
	
}

String::String(const String& s)
{
	//std::cout << "String ������" << std::endl;
	len = s.len;
	str = new char[len];	
	//*
	strcpy_s(str,len,s.str);
}

String::~String()
{
	//std::cout << "~String()" << std::endl;
	if (str != NULL)
	{
		delete str;
	}
}

String& String::operator=(const String& s)
{
	//std::cout << "���������" << std::endl;
	if (str != NULL)
	{
		delete str;
	}
	len = s.len;
	str = new char[len];
	strcpy_s(str, len, s.str);
	return *this;
}

String& String::operator+=(const String& s)
{
	//������ ���ڸ� ������ �迭�� ũ�⸦ ������ �� �� ������ length�� ���� �� null���ڰ� 2���� �ߺ��Ǿ �ϳ��� ��
	len += s.len - 1;	
	char* temp_string = new char[len];
	//strcpy_s(destination, ������ ũ��, source)
	strcpy_s(temp_string, len, str);
	str = new char[len];
	//std::cout << "operator+=��" << std::endl;

	if (str != NULL)
	{
		delete str;
	}
	//strcat_s(destination, destination�� ũ��, source)
	strcat_s(temp_string, len, s.str);
	//std::cout << "operator+=��2" << std::endl;
	str = temp_string;
	//�ڱ��ڽ� return(operator ���������� ��밡���ϰ�)
	return *this;
}

bool String::operator==(const String& s)
{
	//std::cout << "opeator ==" << std::endl;
	//strcmp�� ���ڿ��� ������ false(0)�� return��
	return strcmp(str, s.str) ? false : true;		
}

String String::operator+(const String& s)
{	
	//std::cout << "operator+" << std::endl;
	char* tempstr = new char[len + s.len - 1];	
	strcpy_s(tempstr, len+s.len-1, str);
	strcat_s(tempstr, len+s.len-1, s.str);
	//�ӽð�ü ���� : �����ٷ� �Ѿ�� �����
	String temp(tempstr);
	delete tempstr;

	return temp;
}

std::ostream& operator<< (std::ostream& os,const String& s)
{
	//std::cout << "opearator<<" << std::endl;
	os << s.str;
	return os;
}


std::istream& operator>> (std::istream& is, String& s)
{
	//std::cout << "opearator>>" << std::endl;
	char str[100];
	is >> str;
	s = String(str);
	return is;
}



int main()
{	
	//"I like"�� char�� �迭�� ��
	String str1= "I like";
	String str2 = "string class";
	std::cout << "�ƿ�!" << std::endl;

	String str3 = str1 + str2;


	std::cout << str1 <<std::endl;
	std::cout << str2 << std::endl;
	std::cout << str3 << std::endl;

	str1 += str2;
	if (str1 == str3)
	{
		std::cout << "���� ���ڿ�!" << std::endl;
	}
	else
	{
		std::cout << "�������� ����" << std::endl;
	}

	String str4;
	std::cout<< "���ڿ� �Է� : ";
	std::cin >> str4;
	std::cout << "�Է��� ���ڿ�: " << str4 << std::endl;
	return 0;
}