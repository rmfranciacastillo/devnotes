<?php 

class Vehicle { 

  public $brand;

  public static function create($type, $brand) {
    switch($type) {
      case 'car': 
        return new Car($brand);
      case 'motorcycle': 
        return new Motorbike($brand);
      default:
        throw new Exception("No vehicle found of class $type.");
    }
  }

  public function getType() {
    return get_class($this);
  }
}// end of Vehicle Class 

class Car extends Vehicle {
  public function __construct($brand) {
    $this->brand = $brand;
  }
}// end of Car

class Motorbike  extends Vehicle {

  public function __construct($brand) {
    $this->brand = $brand;
  }
}// end of Motorbike
