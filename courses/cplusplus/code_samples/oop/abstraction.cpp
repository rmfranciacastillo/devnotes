/* Programmer: Renato Francia
 * Description: A simple concept of Abstract classes
 *
 */

#include <iostream>
#include <string>

using std::string;

// Abstract class making requirements to class
// This abstract class will force a developer to use a function
class AbstractCar {
	virtual void Move()=0;
};

// Inherit Abstract class
class Car:AbstractCar {
	private:
		string Status;

	public:
		Car();
		void Move();
};

Car::Car() {
	Status = "staying";
}

void Car::Move() {
	std::cout << "The car is moving" << std::endl;
}

int main() {
	Car c = Car();
	c.Move();
	return 0;
}
