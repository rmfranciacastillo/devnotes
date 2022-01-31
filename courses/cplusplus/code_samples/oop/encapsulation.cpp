/* Programmer: Renato Francia
 * Description: A simple view of encapsulation in C++
 *
 */

#include <iostream>
#include <string>

using std::string;

class Employee {

	private:
		string Name;
		int Age;
		string Role;

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


int main() {

	Employee e1 = Employee("Renato", 18, "Software Engineer");

	e1.Work();
	e1.setRole("Web Developer");
	e1.Work();

	return 0;
}
