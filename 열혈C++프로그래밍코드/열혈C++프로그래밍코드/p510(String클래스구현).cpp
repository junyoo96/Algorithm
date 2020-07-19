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
	//std::cout << "String char 생성자" << std::endl;
	//null문자 하나가 더 들어감
	len = strlen(s) + 1;
	str = new char[len];
	//*	
	//값을 복사
	//std::cout << sizeof(str) << "/"<<sizeof(s) << std::endl;
	//sizeof대신 len을 써주는 이유는 sizeof(str)은 포인터변수의 byte를
	//고정해서 반환하기 때문에 len으로 byte를 할당함
	strcpy_s(str,len, s);
	
}

String::String(const String& s)
{
	//std::cout << "String 생성자" << std::endl;
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
	//std::cout << "복사생성자" << std::endl;
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
	//합쳐진 문자를 저장할 배열의 크기를 결정할 때 각 문자의 length를 더한 뒤 null문자가 2개가 중복되어서 하나를 뺌
	len += s.len - 1;	
	char* temp_string = new char[len];
	//strcpy_s(destination, 복사할 크기, source)
	strcpy_s(temp_string, len, str);
	str = new char[len];
	//std::cout << "operator+=끝" << std::endl;

	if (str != NULL)
	{
		delete str;
	}
	//strcat_s(destination, destination의 크기, source)
	strcat_s(temp_string, len, s.str);
	//std::cout << "operator+=끝2" << std::endl;
	str = temp_string;
	//자기자신 return(operator 연속적으로 사용가능하게)
	return *this;
}

bool String::operator==(const String& s)
{
	//std::cout << "opeator ==" << std::endl;
	//strcmp은 문자열이 같으면 false(0)을 return함
	return strcmp(str, s.str) ? false : true;		
}

String String::operator+(const String& s)
{	
	//std::cout << "operator+" << std::endl;
	char* tempstr = new char[len + s.len - 1];	
	strcpy_s(tempstr, len+s.len-1, str);
	strcat_s(tempstr, len+s.len-1, s.str);
	//임시객체 생성 : 다음줄로 넘어가면 사라짐
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
	//"I like"는 char형 배열로 됨
	String str1= "I like";
	String str2 = "string class";
	std::cout << "아왜!" << std::endl;

	String str3 = str1 + str2;


	std::cout << str1 <<std::endl;
	std::cout << str2 << std::endl;
	std::cout << str3 << std::endl;

	str1 += str2;
	if (str1 == str3)
	{
		std::cout << "동일 문자열!" << std::endl;
	}
	else
	{
		std::cout << "동일하지 않음" << std::endl;
	}

	String str4;
	std::cout<< "문자열 입력 : ";
	std::cin >> str4;
	std::cout << "입력한 문자열: " << str4 << std::endl;
	return 0;
}