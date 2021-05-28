/* Programmer: Renato Francia
 * Description: A simple work in Polymorphism
 */
#include <iostream>
#include <string>

using std::string;

class AbstractEmployee {
	virtual void Work()=0;
};

class Employee : AbstractEmployee {
	private:
		string Name;
		int Age;
	public:
		Employee(string name, int age);
		string getName();
		virtual void Work();
};

Employee::Employee(string name, int age){
	Name = name;
	Age = age;
}

void Employee::Work() {
	std::cout << "Employee: " << Name << " works works and works " << std::endl;
}

string Employee::getName() {
	return Name;
}

class Programmer : public Employee {
	private:
		string Code;
	public:
		Programmer(string name, int age, string code);
		void Work();
};

Programmer::Programmer(string name, int age, string code) : Employee(name, age) {
	Code = code;
}

void Programmer::Work() {
	std::cout << "The programmer " << getName() << " likes to code in " << Code << std::endl;
}

class Teacher : public Employee {
	private:
		string Subject;

	public:
		Teacher(string name, int age, string subject);
};

Teacher::Teacher(string name, int age, string subject) : Employee(name, age) {
	Subject = subject;
}

int main() {

	Programmer p = Programmer("Renato", 31, "C++");
	Teacher t = Teacher("Sarah", 30, "English");

	//p.Work();

	// Polymorphism
	Employee* e1 = &p;
	Employee* e2 = &t;

	e1->Work();
	e2->Work();

	return 0;
}
