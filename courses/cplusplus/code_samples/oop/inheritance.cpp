/* Programmer: Renato Francia
 * Description: Show a simple demo on Inheritance
 *
 */
#include <iostream>
#include <string>

using std::string;

class Employee {

	private:
		int Age;
		string Role;

	protected:
		string Name;

	public:
		Employee();
		Employee(string name, int age, string role);
		void Work();

		// Encapsulation getters and setters
		// Getters
		string getName();
		int getAge();
		string getRole();

		// Setters
		bool setName(string name);
		bool setAge(int age);
		bool setRole(string role);

};

// ctors
Employee::Employee() {
	Name = "";
	Age = 18;
	Role = "employee";
}

Employee::Employee(string name, int age, string role){
	Name = name;
	Age = age;
	Role = role;
}

// Getters
string Employee::getName(){
	return Name;
}

int Employee::getAge() {
	return Age;
}

string Employee::getRole() {
	return Role;
}

// Setters
bool Employee::setName(string name) {
	Name = name;
	return true;
}

bool Employee::setAge(int age) {
	Age = age;
	return true;
}

bool Employee::setRole(string role) {
	Role = role;
	return true;
}


void Employee::Work() {
	std::cout << Name << " is " << Age << " years old. And he works as a "
		<< Role << std::endl;
}

// Inherit from Employee
class Programmer:Employee {
	private:
		string Code;

	public:
		Programmer(string name, int age, string role, string code);
		void Work();
};

Programmer::Programmer(string name, int age, string role, string code)
			:Employee(name, age, role) {
	Code = code;
}

void Programmer::Work() {
	std::cout << Name << " is working with " << Code << std::endl;
}

int main() {

	Programmer p = Programmer("Renato", 31, "Programmer", "C++");

	p.Work();

	return 0;
}
